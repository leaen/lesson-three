from django.shortcuts import render

from .models import Entry
from .models import Client
from .models import Project


def entries(request):
    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
    })

def clients(request):
    client_list = Client.objects.all()
    return render(request, 'clients.html', {
        'client_list': client_list,
    })

def projects(request):
    project_list = Project.objects.all()
    return render(request, 'projects.html', {
        'project_list': project_list,
    })
