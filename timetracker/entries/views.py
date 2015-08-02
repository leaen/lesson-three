from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotFound

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

def client(request):
    client_id = request.GET.get('client_id')
    if client_id:
        try:
            client_id = int(client_id)
        except BaseException:
            # client_id should be an integer, return a 400
            raise HttpResponseBadRequest

        client = Client.objects.filter(id=client_id)[0]
        project_list = Project.objects.filter(client=client)
        entry_dict = {}
        for project in project_list:
            entries = Entry.objects.filter(project=project)
            entry_dict[project.id] = entries

        return render(request, 'client.html', {
            'client': client,
            'project_list': project_list,
            'entry_dict': entry_dict,
        })
    else:
        raise HttpResponseNotFound
