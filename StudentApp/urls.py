from django.conf.urls import url

from . import views

app_name = 'StudentApp'
urlpatterns = [
    # /students
    url(r'^$', views.SchoolView.as_view(), name='school'),
    # /students/api/studentautocomplete
    url(r'^api/studentautocomplete/$', views.StudentAutoComplete.as_view(), name='student-autocomplete'),
    # /students/schoolname
    url(r'^(?P<slug>[\w-]+)/$', views.HouseView.as_view(), name='house'),
    # /students/schoolname/housename
    url(r'^(?P<slug>[\w-]+)/(?P<house_slug>[\w-]+)/$', views.StudentView.as_view(), name='student'),
]
