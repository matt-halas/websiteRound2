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
    return render(request, 'website/project.html', {
        'content': markdown(entry)
    })
