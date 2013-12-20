from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

from info.models import Brother
from info import utility

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
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.filter(isAlumni=isAlumniFilter, isPledge=isPledgeFilter).order_by('lastName', 'firstName', 'middleName')
    if len(brothers) > 0:
        brother_list_list = utility.convert_array_to_Yx3(brothers)
    else:
        brother_list_list = None
    c = Context({'brotherType': name, 'brother_list_list' : brother_list_list})
    return HttpResponse(t.render(c))
