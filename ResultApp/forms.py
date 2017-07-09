from django.forms import ModelForm, modelformset_factory, DurationField, CharField
from dal import autocomplete
from ResultApp.models import *
from django import forms


class CrossCountryResultForm(ModelForm):
    class Meta:
        model = CrossCountryResult
        fields = ['event', 'student', 'position', 'house_points', ]
        widgets = {
            'student': autocomplete.ModelSelect2(url='StudentApp:student-autocomplete')
        }


class TrackEventResultForm(ModelForm):
    time = CharField(required=False)

    class Meta:
        model = TrackEventResult
        fields = ['event', 'student', 'time', 'house_points', ]
        widgets = {
            'student': autocomplete.ModelSelect2(url='StudentApp:student-autocomplete'),
        }


class FieldEventResultForm(ModelForm):
    class Meta:
        model = FieldEventResult
        fields = ['event', 'student', 'distance', 'house_points', ]
        widgets = {
            'student': autocomplete.ModelSelect2(url='StudentApp:student-autocomplete')
        }


class SwimmingResultForm(ModelForm):
    time = DurationField(required=False)

    class Meta:
        model = SwimmingResult
        fields = ['event', 'student', 'time', 'house_points', ]
        widgets = {
            'student': autocomplete.ModelSelect2(url='StudentApp:student-autocomplete')
        }


class TrackRelayResultForm(ModelForm):
    time = DurationField(required=False)

    class Meta:
        model = TrackRelayResult
        fields = ['house', 'event', 'time', 'house_points', ]


class SwimmingRelayResultForm(ModelForm):
    time = DurationField(required=False)

    class Meta:
        model = SwimmingRelayResult
        fields = ['house', 'event', 'time', 'house_points', ]


CrossCountryResultFormSet = modelformset_factory(CrossCountryResult, form=CrossCountryResultForm, extra=10)
TrackEventResultFormSet = modelformset_factory(TrackEventResult, form=TrackEventResultForm, extra=8)
TrackRelayResultFormSet = modelformset_factory(TrackRelayResult, form=TrackRelayResultForm, extra=3)
FieldEventResultFormSet = modelformset_factory(FieldEventResult, form=FieldEventResultForm, extra=6)
SwimmingResultFormSet = modelformset_factory(SwimmingResult, form=SwimmingResultForm, extra=6)
SwimmingRelayResultFormSet = modelformset_factory(SwimmingRelayResult, form=SwimmingRelayResultForm, extra=3)
