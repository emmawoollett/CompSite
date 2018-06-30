from django.contrib import admin
from .models import *


class CrossCountryInline(admin.TabularInline):
    model = CrossCountry
    extra = 0


class TrackEventInline(admin.TabularInline):
    model = TrackEvent
    extra = 0


class TrackRelayInline(admin.TabularInline):
    model = TrackRelay
    extra = 0


class FieldEventInline(admin.TabularInline):
    model = FieldEvent
    extra = 0


class SwimmingInLine(admin.TabularInline):
    model = Swimming
    extra = 0


class SwimmingRelayInline(admin.TabularInline):
    model = SwimmingRelay
    extra = 0


class CompetitionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('competition_name',)}
    fields = ['competition_name', 'competition_date', 'slug', 'junior_year_groups']
    list_display = ('competition_name', 'competition_date')
    list_filter = ['competition_date']
    search_fields = ['competition_name']
    inlines = [CrossCountryInline, TrackEventInline, TrackRelayInline, FieldEventInline, SwimmingInLine,
               SwimmingRelayInline]


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(CrossCountry)
admin.site.register(TrackEvent)
admin.site.register(TrackRelay)
admin.site.register(FieldEvent)
admin.site.register(Swimming)
admin.site.register(SwimmingRelay)
