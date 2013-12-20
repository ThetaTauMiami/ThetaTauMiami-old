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
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.filter(isAlumni=False, isPledge=False).order_by('-lastName')
    if len(brothers) > 0:
        brother_list_list = utility.convert_array_to_Yx3(brothers)
    else:
        brother_list_list = None
    c = Context({'brotherType': 'Active Members', 'brother_list_list' : brother_list_list})
    return HttpResponse(t.render(c))

def pledges(request):
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.filter(isPledge=True)
    if len(brothers) > 0:
        brother_list_list = utility.convert_array_to_Yx3(brothers)
    else:
        brother_list_list = None
    c = Context({'brotherType': 'Pledges', 'brother_list_list' : brother_list_list})
    return HttpResponse(t.render(c))

def alumni(request):
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.filter(isAlumni=True)
    if len(brothers) > 0:
        brother_list_list = utility.convert_array_to_Yx3(brothers)
    else:
        brother_list_list = None
    c = Context({'brotherType': 'Alumni', 'brother_list_list' : brother_list_list})
    return HttpResponse(t.render(c))
