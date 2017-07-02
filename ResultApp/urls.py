from django.conf.urls import url

from . import views

app_name = 'ResultApp'
urlpatterns = [
    # /results
    url(r'^$', views.ResultIndexView.as_view(), name='resultindex'),
    # /results/competition_name
    url(r'^(?P<slug>[\w-]+)/$', views.ResultDetailView.as_view(), name='resultdetail'),

    # /results/competition_name/students
    url(r'^(?P<slug>[\w-]+)/students/$', views.StudentResultDetailView.as_view(), name='student-analysis'),
    # /results/competition_name/houses
    url(r'^(?P<slug>[\w-]+)/houses/$', views.HouseResultDetailView.as_view(), name='house-analysis'),

    # /results/event_type/event_slug/createresult
    url(r'^(?P<event_type>[\w-]+)/(?P<event_slug>[\w-]+)/createresult/$', views.EventResultCreate.as_view(), name='event-result'),
    # /results/event_type/event_slug/printresult
    url(r'^(?P<event_type>[\w-]+)/(?P<event_slug>[\w-]+)/printresult/$', views.EventResultPrint.as_view(),
        name='print-event-result'),

]
