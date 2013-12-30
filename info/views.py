from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

from info.models import Brother
from info import utility

max_brothers_per_page = 24

# Create your views here.
def index(request):
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.all()
    if len(brothers) > 0:
        brother_list_list = utility.convert_array_to_Yx3(brothers)
    else:
        brother_list_list = None
    c = Context({'brotherType': 'All Brothers', 'brother_list_list' : brother_list_list})
    return HttpResponse(t.render(c))


def officers(request):
    t = loader.get_template('brothers_list.html')
    brothers = None
    c = Context({'brotherType': 'Officers', 'brother_list' : brothers})
    return HttpResponse(t.render(c))

def actives(request):
    return general_listing(request, False, False, 'Active Members')

def pledges(request):
    return general_listing(request, False, True, 'Pledges')

def alumni(request):
    return general_listing(request, True, False, 'Alumni')

def general_listing(request, isAlumniFilter, isPledgeFilter, name):
    brothers_count = request.GET.get('count','9')
    try:
        brothers_count = int(brothers_count)
        if brothers_count > max_brothers_per_page:
            brothers_count = max_brothers_per_page
    except:
        brothers_count = 9
    page_number = request.GET.get('page','1')
    try:
        page_number = int(page_number)
    except:
        page_number = 1
    brothers_range_min = (page_number - 1) * brothers_count
    brothers_range_max = (page_number) * brothers_count
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.filter(isAlumni=isAlumniFilter, isPledge=isPledgeFilter).order_by('lastName', 'firstName', 'middleName')[brothers_range_min:brothers_range_max]
    if len(brothers) > 0:
        brother_list_list = utility.convert_array_to_Yx3(brothers)
    else:
        brother_list_list = None
    page_numbers_list = range(1,6)
    next_page = page_number + 1
    prev_page = page_number - 1
    context_dict = {'brotherType': name, 'brother_list_list' : brother_list_list, 'page_number' : page_number, 'prev_page': prev_page, 'next_page' : next_page, 'page_numbers' : page_numbers_list}
    if brothers_count != 9:
        context_dict['brothers_count'] = brothers_count
    c = Context(context_dict)
    return HttpResponse(t.render(c))
