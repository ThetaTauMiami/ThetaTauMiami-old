import math
from datetime import date

from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from info.models import Brother, Officer, BrotherEntity, Major, Job
from info import utility
from marketing.models import Picture as MarketingPic
from articles.models import Article
from listing.pages import PageHelper

max_brothers_per_page = 24
standard_brothers_per_page = 9
brothers_per_row = 3
max_pages_listed_on_screen = 5
officers_per_row = 2
exec_board_members_per_row_on_about_page = 3


def index(request):
    t = loader.get_template('about.html')
    officer_list = Officer.objects.filter().order_by('ordering')
    group_pic = MarketingPic.objects.filter(name='Group')[0]
    recent_events = Article.objects.all().order_by('-date')[:6]
    c = Context({'officer_list': officer_list, 'group_pic': group_pic, 'articles': recent_events})
    return HttpResponse(t.render(c))

def brother_profile(request, brother_id):
    bro = get_object_or_404(Brother, pk = brother_id)
    return render(request, 'brother_profile.html', {'be': BrotherEntity(bro)})

def officers(request):
    officers = Officer.objects.filter().order_by('ordering')
    officers_matrix = utility.convert_array_to_YxZ(officers, officers_per_row)
    c = Context({'officer_list_list': officers_matrix})
    t = loader.get_template('officers_list.html')
    return HttpResponse(t.render(c))

def actives(request):
    return general_listing(request, False, False, 'Active Members')

def pledges(request):
    return general_listing(request, False, True, 'Pledges')

def alumni(request):
    return general_listing(request, True, False, 'Alumni')

def general_listing(request, isAlumniFilter, isPledgeFilter, name):
    '''
    Retrieves all of the information necessary for each of the brother listings.
    Retrieves information based on the isAlumniFilter and isPledgeFilter
    '''
    brothers_count = PageHelper.get_request_count(request, standard_brothers_per_page, max_brothers_per_page)
    page_number = PageHelper.get_page_number(request)
    brothers_range_min = (page_number - 1) * brothers_count
    brothers_range_max = (page_number) * brothers_count
    brothers = Brother.objects.filter(isAlumni=isAlumniFilter, isPledge=isPledgeFilter).order_by(
        'lastName', 'firstName', 'middleName')
    number_of_brothers = len(brothers)
    total_pages = int(math.ceil(number_of_brothers / float(brothers_count)))
    brothers = brothers[brothers_range_min:brothers_range_max]
    brothers = convert_brothers_to_brotherentities(brothers)
    brother_list_list = utility.convert_array_to_YxZ(brothers, brothers_per_row) if len(brothers) > 0 else None
    page_numbers_list = PageHelper.calculate_page_range(total_pages, page_number, max_pages_listed_on_screen)
    next_page = page_number + 1 if number_of_brothers > brothers_range_max else 0
    prev_page = page_number - 1
    context_dict = {
                    'brotherType': name, 
                    'brother_list_list' : brother_list_list, 
                    'page_number' : page_number, 
                    'prev_page': prev_page, 
                    'next_page' : next_page, 
                    'page_numbers' : page_numbers_list
                    }
    if brothers_count != standard_brothers_per_page:
        context_dict['brothers_count'] = brothers_count
    c = Context(context_dict)
    t = loader.get_template('brothers_list.html')
    return HttpResponse(t.render(c))

def resumes(request):
    year = date.today().year
    years = []
    for i in xrange(5):
        years.append(year+i)
    grad_year_requests = request.GET.getlist('gradyear')
    reqs = Q()
    for grad_year_request in grad_year_requests:
        reqs = reqs | Q(graduationYear=int(grad_year_request))
    brothers = Brother.objects.filter(reqs).order_by('lastName', 'firstName', 'middleName')
    majors = Major.objects.all().order_by('majorName')
    c = Context({'brothers': brothers, 'majors': majors, 'years': years})
    t = loader.get_template('resume_list.html')
    return HttpResponse(t.render(c))

def careers(request):
    jobs = Job.objects.all()
    return render(request, 'careers.html', {'jobs': jobs})

def convert_brothers_to_brotherentities(broList):
    '''
    Converts a set of brothers and converts them to brother entities 
    which contain more information
    '''
    broEList = []
    for bro in broList:
        broEList.append(BrotherEntity(bro))
    return broEList
