from django.shortcuts import render
from projects.models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)

def details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'details.html', context)
