from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.http import Http404
from django.views import generic
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .forms import *
from StudentApp.models import House
from .models import ResultsModels, RelayResultModels
from CompApp.models import Event, TrackEvent
import CompApp


class ResultIndexView(generic.ListView):
    template_name = 'ResultApp/resultindex.html'
    model = Competition


class ResultDetailView(generic.DetailView):
    template_name = 'ResultApp/resultdetail.html'
    model = Competition

    def get_context_data(self, **kwargs):
        context = super(ResultDetailView, self).get_context_data(**kwargs)
        competition = self.get_object()
        houses = House.objects.all()
        junior_boys = self.get_results(competition, [Event.YEAR_7, Event.YEAR_8], [Event.BOYS], houses)
        junior_girls = self.get_results(competition, [Event.YEAR_7, Event.YEAR_8,], [Event.GIRLS], houses)
        senior_boys = self.get_results(
            competition, [Event.YEAR_9, Event.YEAR_10, Event.YEAR_11], [Event.BOYS], houses
        )
        senior_girls = self.get_results(
            competition, [Event.YEAR_9, Event.YEAR_10, Event.YEAR_11], [Event.GIRLS], houses
        )
        overall = self.get_results(
            competition,
            [Event.YEAR_7, Event.YEAR_8, Event.YEAR_9, Event.YEAR_10, Event.YEAR_11],
            [Event.BOYS, Event.GIRLS], houses
        )
        table = [
            ['', 'Roman', 'Trojan', 'Spartan'],
            ['Junior boys', junior_boys['Roman'], junior_boys['Trojan'], junior_boys['Spartan']],
            ['Junior girls', junior_girls['Roman'], junior_girls['Trojan'], junior_girls['Spartan']],
            ['Senior boys', senior_boys['Roman'], senior_boys['Trojan'], senior_boys['Spartan']],
            ['Senior girls', senior_girls['Roman'], senior_girls['Trojan'], senior_girls['Spartan']],
            ['Overall', overall['Roman'], overall['Trojan'], overall['Spartan']],
        ]
        context['table'] = table
        return context

    def get_results(self, competition, years, genders, houses):
        house_totals = {}
        for house in houses:
            house_totals[house.house_name] = 0

        for model in ResultsModels:
            all_results = model.objects.filter(
                event__gender__in=genders, event__competition=competition, event__year_group__in=years
            )
            sum_house_points = all_results.values('student__house__house_name').annotate(total=Sum('house_points'))
            for house_points in sum_house_points:
                house_name = house_points['student__house__house_name']
                house_total = house_points['total']
                house_totals[house_name] += house_total

        for model in RelayResultModels:
            relay_results = model.objects.filter(
                event__gender__in=genders, event__competition=competition, event__year_group__in=years
            )
            sum_house_points = relay_results.values('house__house_name').annotate(total=Sum('house_points'))
            for house_points in sum_house_points:
                house_name = house_points['house__house_name']
                house_total = house_points['total']
                house_totals[house_name] += house_total

        return house_totals


class StudentResultDetailView(generic.DetailView):
    template_name = 'ResultApp/studentanalysis.html'
    model = Competition

    def get_context_data(self, **kwargs):
        context = super(StudentResultDetailView, self).get_context_data(**kwargs)
        competition = self.get_object()
        year_7_boys = self.get_students(competition, [Event.YEAR_7], Student.BOYS)
        year_7_girls = self.get_students(competition, [Event.YEAR_7], Student.GIRLS)
        year_8_boys = self.get_students(competition, [Event.YEAR_8], Student.BOYS)
        year_8_girls = self.get_students(competition, [Event.YEAR_8], Student.GIRLS)
        year_9_boys = self.get_students(competition, [Event.YEAR_9], Student.BOYS)
        year_9_girls = self.get_students(competition, [Event.YEAR_9], Student.GIRLS)
        senior_boys = self.get_students(competition, [Event.YEAR_10, Event.YEAR_11], Student.BOYS)
        senior_girls = self.get_students(competition, [Event.YEAR_10, Event.YEAR_11], Student.GIRLS)

        def div_students(year_gender):
            return mark_safe(''.join(['<div> %s - %s </div>' % student for student in year_gender]))

        table = [
            ['', 'Boys', 'Girls'],
            ['Year 7', div_students(year_7_boys), div_students(year_7_girls)],
            ['Year 8', div_students(year_8_boys), div_students(year_8_girls)],
            ['Year 9', div_students(year_9_boys), div_students(year_9_girls)],
            ['Year 10/11', div_students(senior_boys), div_students(senior_girls)]
        ]
        context['table'] = table
        return context

    def get_students(self, competition, years, gender):
        top_students = {}
        for model in ResultsModels:
            results = model.objects.filter(
                event__year_group__in=years, student__gender=gender, event__competition=competition
            )
            top_results = results.values('student').annotate(
                house_points=Sum('house_points')
            ).order_by('-house_points')
            for top_result in top_results:
                house_points = top_result['house_points']
                student = top_result['student']
                running_total = top_students.get(student, 0)
                running_total+=house_points
                top_students[student]=running_total
        top_five_students = sorted(top_students, key=lambda s: top_students[s], reverse=True)[0:5]
        top_five_student_tuple = [
            (Student.objects.get(id=student_id), top_students[student_id]) for student_id in top_five_students
        ]
        return top_five_student_tuple


class HouseResultDetailView(generic.DetailView):
    template_name = 'ResultApp/houseanalysis.html'
    model = Competition

    def get_context_data(self, **kwargs):
        context = super(HouseResultDetailView, self).get_context_data(**kwargs)
        competition = self.get_object()
        houses = House.objects.all()
        winners = []
        for house in houses:
            student_winners = house.get_student_winners(competition.competition_name)
            winners.append((house, student_winners))
            for student in student_winners:
                generator = student.get_winner_events(competition.competition_name)
                setattr(student, 'winner_events', generator)
        context['student_winners'] = winners
        return context


class EventResultCreate(generic.TemplateView):
    template_name = 'ResultApp/eventresult.html'

    def post(self, request, *args, **kwargs):
        formset_class, model_class = self.get_formset_class(**kwargs)
        event_slug = kwargs['event_slug']
        event = model_class.objects.get(slug=event_slug)
        formset = formset_class(request.POST, request.FILES, initial=[{'id':'event_id'}])
        if formset.is_valid():
            formset.save()
            url = reverse('ResultApp:event-result', kwargs=kwargs)
            return redirect(url)
        else:
            return render(request, self.template_name, {'formset': formset, 'event': event})

    def get(self, request, *args, **kwargs):
        formset_class, model_class = self.get_formset_class(**kwargs)
        event_slug = kwargs['event_slug']
        event = model_class.objects.get(slug=event_slug)
        result_class = formset_class.model
        results_for_event = result_class.objects.filter(event__slug=event_slug)
        formset = formset_class(queryset=results_for_event)

        for form in formset:
            form.fields['event'].initial = event
            if 'time' in form.fields:
                form.fields['time'].widget.attrs['tabindex'] = 2
            if 'distance' in form.fields:
                form.fields['distance'].widget.attrs['tabindex'] = 2
            form.fields['house_points'].widget.attrs['tabindex'] = 3

        return render(request, self.template_name, {'formset': formset, 'event': event})

    def get_formset_class(self, **kwargs):
        event_type = kwargs['event_type']
        my_class = getattr(CompApp.models, event_type)
        if my_class == CrossCountry:
            formset_class = CrossCountryResultFormSet
        elif my_class == TrackEvent:
            formset_class = TrackEventResultFormSet
        elif my_class == FieldEvent:
            formset_class = FieldEventResultFormSet
        elif my_class == TrackRelay:
            formset_class = TrackRelayResultFormSet
        elif my_class == Swimming:
            formset_class = SwimmingResultFormSet
        elif my_class == SwimmingRelay:
            formset_class = SwimmingRelayResultFormSet
        else:
            raise Http404
        return formset_class, my_class


class EventResultPrint(generic.TemplateView):
    template_name = 'ResultApp/printeventresult.html'

    def get(self, request, *args, **kwargs):
        model_class = self.get_model_class(**kwargs)
        event_slug = kwargs['event_slug']
        event = model_class.objects.get(slug=event_slug)
        lane_draw = [1, 8, 2, 7, 3, 6, 4, 5]
        if model_class == CrossCountry:
            event_results = CrossCountryResult.objects.filter(event=event)
            headers = ['House points','', 'Name', 'Position']
        elif model_class == TrackEvent:
            event_results = TrackEventResult.objects.filter(event=event)
            if event.track_choice == TrackEvent.HEATS:
                headers = ['Lane draw', 'House', 'Name', 'Time']
            else:
                headers = ['House points', 'House', 'Name', 'Time']
        elif model_class == FieldEvent:
            event_results = FieldEventResult.objects.filter(event=event)
            headers = ['House points', 'House', 'Name', 'Distance']
        elif model_class == TrackRelay:
            event_results = TrackRelayResult.objects.filter(event=event)
            headers = ['House points','','House', 'Time']
        elif model_class == Swimming:
            event_results = SwimmingResult.objects.filter(event=event)
            headers = ['House points', 'House', 'Name', 'Time']
        elif model_class == SwimmingRelay:
            event_results = SwimmingRelayResult.objects.filter(event=event)
            headers = ['House points','','House', 'Time']
        else:
            raise Http404
        return render(
            request, self.template_name,
            {'event': event, 'event_results':event_results, 'headers':headers, 'lane_draw':lane_draw}
        )

    def get_model_class(self, **kwargs):
        event_type = kwargs['event_type']
        my_class = getattr(CompApp.models, event_type)
        return my_class