from django.conf.urls import url

from . import views

urlpatterns = [
    #www.web.com
    url(r'^$', views.index, name='index'),
    
    #www.web.com/journals
    url(r'^journals/$', views.journals, name='journals'),
    
    #www.web.com/create
    url(r'^create/$', views.journal_create, name='journal_create'),
    
    #www.web.com/journal/1234
    url(r'^journal/(?P<journal_id>[0-9]+)/$', views.journal_view, name='journal_view'),
    
    #www.web.com/journal/1234/create
    url(r'^journal/(?P<journal_id>[0-9]+)/create/$', views.entry_create, name='entry_create'),
    
    #www.web.com/journal/1234/entry/1234
    url(r'^journal/(?P<journal_id>[0-9]+)/entry/(?P<entry_id>[0-9]+)/$', views.entry_view, name='entry_view'),
        
    #www.web.com/journal/1234/edit/1234
    url(r'^journal/(?P<journal_id>[0-9]+)/edit/(?P<entry_id>[0-9]+)/$', views.entry_edit, name='entry_edit'),
        
    #www.web.com/journal/1234/history/1234
    url(r'^journal/(?P<journal_id>[0-9]+)/history/(?P<entry_id>[0-9]+)/$', views.entry_history, name='entry_history'),
]

