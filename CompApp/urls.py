from django.conf.urls import url

from . import views

app_name = 'CompApp'
urlpatterns = [
    # /comp
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /comp/competition_name
    url(r'^(?P<slug>[\w-]+)/$', views.DetailView.as_view(), name='detail'),
    # /comp/competition_name/event_type/add
    url(r'^(?P<slug>[\w-]+)/(?P<event_type>[\w-]+)/add/$', views.AddEvent.as_view(), name='event'),
    # /comp/competition_name/event_type/delete
    url(r'^(?P<pk>[\w-]+)/(?P<event_type>[\w-]+)/delete/$', views.DeleteEvent.as_view(), name='delete-event'),
]
