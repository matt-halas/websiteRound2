from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .util import get_entry
from markdown2 import markdown

# Create your views here.


def index(request):
    return render(request, 'website/index.html')


def projectView(request, projectTitle):
    entry = get_entry(projectTitle)
    if entry != None:
        return render(request, 'website/project.html', {
            'content': markdown(entry)
        })
    else:
        return render(request, 'website/project.html')


def fluidSim(request):
    return render(request, 'website/fluidSim.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    return render(request, 'website/contact.html')


def resume(request):
    return render(request, 'website/resume.html')
