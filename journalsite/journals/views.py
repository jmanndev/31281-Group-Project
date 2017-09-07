from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import datetime
from django.urls import reverse

from .models import Journal, User, Entry, EntryLog

def index(request):
    return HttpResponse("Hi world")

def journals(request):
    journal_list = Journal.objects.order_by('created_date')
    template = loader.get_template('journals/journals_all.html')
    context = {
        'journal_list': journal_list,
    }
    return HttpResponse(template.render(context,request))
    
def journal_create(request):
    template = loader.get_template('journals/create_journal.html')
    context = {    }
    return HttpResponse(template.render(context,request))
    
def journal_create_confirm(request):
    j = Journal(
        author=User.objects.get(pk=1), #debug
        name_text=request.POST.get('name'),
        description_text=request.POST.get('description'),
        created_date=datetime.datetime.now(),
        modified_date=datetime.datetime.now()
    )
    j.save()
    return HttpResponseRedirect(reverse('journals:journals'))    
    
def journal_view(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    entry_list = EntryLog.objects.filter(journal=journal_id)
    template = loader.get_template('journals/view_journal.html')
    context = {
        'journal': journal,
    }
    return HttpResponse(template.render(context, request))
    
def entry_create(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    template = loader.get_template('journals/create_entry.html')
    context = {
        'journal': journal,
    }
    return HttpResponse(template.render(context, request))
    
def entry_create_confirm(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    context = {
        'journal': journal,
    }
    el = EntryLog(
        journal=Journal.objects.get(pk=journal_id)
    )
    el.save()
    e = Entry(
        entry_log=el,
        title_text=request.POST.get('name'),
        body_text=request.POST.get('description'),
        published_date=datetime.datetime.now(),
        hidden_boolean=False,
        deleted_boolean=False
    )
    e.save()
    return HttpResponseRedirect(reverse('journals:journal_view', args=(journal_id)))   

def entry_view(request, journal_id, entry_id):
    return HttpResponse("view entry %s" % entry_id)
    
def entry_edit(request, journal_id, entry_id):
    return HttpResponse("edit entry %s" % entry_id)
    
def entry_history(request, journal_id, entry_id):
    return HttpResponse("entry history %s" % entry_id)