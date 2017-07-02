from django.contrib import admin
from .models import *


class CrossCountryResultAdmin(admin.ModelAdmin):
    fields = ['event', 'student', 'position', 'house_points']
    list_display = ('event', 'student', 'position', 'house_points')
    list_filter = ['event']
    search_fields = ['student']


class TrackEventResultAdmin(admin.ModelAdmin):
    fields = ['event', 'student', 'time', 'house_points']
    list_display = ('event', 'student', 'time', 'house_points')
    list_filter = ['event']
    search_fields = ['student']


class FieldEventResultAdmin(admin.ModelAdmin):
    fields = ['event', 'student', 'distance', 'house_points']
    list_display = ('event', 'student', 'distance', 'house_points')
    list_filter = ['event']
    search_fields = ['student']


class SwimmingResultAdmin(admin.ModelAdmin):
    fields = ['event', 'student', 'time', 'house_points']
    list_display = ('event', 'student', 'time', 'house_points')
    list_filter = ['event']
    search_fields = ['student']


class TrackRelayResultAdmin(admin.ModelAdmin):
    fields = ['event', 'house', 'time', 'house_points']
    list_display = ('event', 'house', 'time', 'house_points')
    list_filter = ['event']
    search_fields = ['house']


class SwimmingRelayResultAdmin(admin.ModelAdmin):
    fields = ['event', 'house', 'time', 'house_points']
    list_display = ('event', 'house', 'time', 'house_points')
    list_filter = ['event']
    search_fields = ['house']

admin.site.register(CrossCountryResult, CrossCountryResultAdmin)
admin.site.register(TrackEventResult, TrackEventResultAdmin)
admin.site.register(FieldEventResult, FieldEventResultAdmin)
admin.site.register(SwimmingResult, SwimmingResultAdmin)
admin.site.register(TrackRelayResult, TrackRelayResultAdmin)
admin.site.register(SwimmingRelayResult, SwimmingRelayResultAdmin)
