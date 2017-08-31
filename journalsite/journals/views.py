from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi world")

def journals(request):
    return HttpResponse("all journals list")
    
def journal_create(request):
    return HttpResponse("create journal form")
    
def journal_view(request, journal_id):
    return HttpResponse("view journal %s" % journal_id)
    
def entry_create(request, journal_id):
    return HttpResponse("create entry form")
    
def entry_view(request, journal_id, entry_id):
    return HttpResponse("view entry %s" % entry_id)
    
def entry_edit(request, journal_id, entry_id):
    return HttpResponse("edit entry %s" % entry_id)
    
def entry_history(request, journal_id, entry_id):
    return HttpResponse("entry history %s" % entry_id)