from django.urls import reverse
from django.views import generic
from django.apps import apps

from .models import Competition


class IndexView(generic.ListView):
    template_name = 'CompApp/index.html'
    model = Competition


class DetailView(generic.DetailView):
    template_name = 'CompApp/detail.html'
    model = Competition


class AddEvent(generic.CreateView):
    template_name = 'CompApp/event.html'
    fields = '__all__'

    def get_queryset(self):
        # looks up a model from CompApp. To find model name can use the print function to see kwargs:
        # print(self.kwargs)
        event = apps.get_model(app_label='CompApp', model_name=self.kwargs['event_type'])
        return event.objects.all()

    def get_success_url(self):
        # returns you to the detail page once data has been submitted
        return reverse('CompApp:detail', kwargs={'slug': self.kwargs['slug']})


class DeleteEvent(generic.DeleteView):
    template_name = 'CompApp/event.html'

    def get_object(self, queryset=None):
        # print(self.request.META)
        events = apps.get_model(app_label='CompApp', model_name=self.kwargs['event_type'])
        return events.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('CompApp:index')
