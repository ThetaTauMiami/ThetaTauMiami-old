from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

from info.models import Brother

# Create your views here.
def index(request):
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects
    c = Context({'brotherType': 'All Brothers', 'brother_list' : brothers})
    return HttpResponse(t.render(c))


def officers(request):
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.filter(lastName='Rogers')
    c = Context({'brotherType': 'Officers', 'brother_list' : brothers})
    return HttpResponse(t.render(c))

def actives(request):
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.filter(isAlumni=False, isPledge=False)
    c = Context({'brotherType': 'Active Members', 'brother_list' : brothers})
    return HttpResponse(t.render(c))

def pledges(request):
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.filter(isPledge=True)
    c = Context({'brotherType': 'Pledges', 'brother_list' : brothers})
    return HttpResponse(t.render(c))

def alumni(request):
    t = loader.get_template('brothers_list.html')
    brothers = Brother.objects.filter(isAlumni=True)
    c = Context({'brotherType': 'Alumni', 'brother_list' : brothers})
    return HttpResponse(t.render(c))