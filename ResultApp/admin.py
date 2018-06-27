from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import *


class CrossCountryResultAdmin(admin.ModelAdmin):
    fields = ['event', 'student', 'position', 'house_points']
    list_display = ('event', 'student', 'position', 'house_points')
    list_filter = ['event']
    search_fields = ['student']


class TrackEventResultResource(resources.ModelResource):
    year_group = fields.Field(column_name='year', attribute='event', widget=ForeignKeyWidget(Event, 'year_group'))
    distance = fields.Field(column_name='distance in meters', attribute='event',
                            widget=ForeignKeyWidget(Event, 'distance_in_meters'))
    gender = fields.Field(column_name='gender', attribute='event', widget=ForeignKeyWidget(Event, 'gender'))
    track_choice = fields.Field(column_name='heat/final', attribute='event',
                                widget=ForeignKeyWidget(Event, 'track_choice'))
    first_name = fields.Field(column_name='first name', attribute='student',
                              widget=ForeignKeyWidget(Student, 'first_name'))
    last_name = fields.Field(column_name='last name', attribute='student',
                              widget=ForeignKeyWidget(Student, 'last_name'))

    class Meta:
        model = TrackEventResult
        fields = ('year_group', 'distance', 'gender', 'track_choice', 'first_name', 'last_name', 'time')
        export_order = ('year_group', 'distance', 'gender', 'track_choice', 'first_name', 'last_name', 'time')
        import_id_fields = ['student']

    def dehydrate_gender(self, trackeventresult):
        return trackeventresult.event.get_gender_display()

    def dehydrate_track_choice(self, trackeventresult):
        return trackeventresult.event.get_track_choice_display()


class TrackEventResultAdmin(ImportExportModelAdmin):
    resource_class = TrackEventResultResource
    fields = ['event', 'student', 'time', 'house_points']
    list_display = ('event', 'student', 'time', 'house_points')
    list_filter = ['event']
    search_fields = ['student']


class FieldEventResultResource(resources.ModelResource):
    year_group = fields.Field(column_name='year group', attribute='event', widget=ForeignKeyWidget(Event, 'year_group'))
    field_name = fields.Field(column_name='event type', attribute='event',
                               widget=ForeignKeyWidget(Event, 'field_name'))
    gender = fields.Field(column_name='gender', attribute='event', widget=ForeignKeyWidget(Event, 'gender'))
    first_name = fields.Field(column_name='first name', attribute='student',
                              widget=ForeignKeyWidget(Student, 'first_name'))
    last_name = fields.Field(column_name='last name', attribute='student',
                              widget=ForeignKeyWidget(Student, 'last_name'))

    class Meta:
        model = FieldEventResult
        fields = ('year_group', 'field_name', 'gender', 'first_name', 'last_name', 'distance')
        export_order = ('year_group', 'field_name', 'gender', 'first_name', 'last_name', 'distance')
        import_id_fields = ['student']

    def dehydrate_gender(self, trackeventresult):
        return trackeventresult.event.get_gender_display()

    def dehydrate_field_name(self, trackeventresult):
        return trackeventresult.event.get_field_name_display()


class FieldEventResultAdmin(ImportExportModelAdmin):
    resource_class = FieldEventResultResource
    fields = ['event', 'student', 'distance', 'house_points']
    list_display = ('event', 'student', 'distance', 'house_points')
    list_filter = ['event']
    search_fields = ['student']


class SwimmingResultResource(resources.ModelResource):
    year_group = fields.Field(column_name='year group', attribute='event', widget=ForeignKeyWidget(Event, 'year_group'))
    gender = fields.Field(column_name='gender', attribute='event', widget=ForeignKeyWidget(Event, 'gender'))
    stroke = fields.Field(column_name='stroke', attribute='event',
                            widget=ForeignKeyWidget(Event, 'stroke'))
    first_name = fields.Field(column_name='first name', attribute='student',
                              widget=ForeignKeyWidget(Student, 'first_name'))
    last_name = fields.Field(column_name='last name', attribute='student',
                              widget=ForeignKeyWidget(Student, 'last_name'))

    class Meta:
        model = SwimmingResult
        fields = ('year_group', 'gender', 'stroke', 'first_name', 'last_name', 'time')
        export_order = ('year_group', 'gender', 'stroke', 'first_name', 'last_name', 'time')
        import_id_fields = ['student']

    def dehydrate_gender(self, swimmingresult):
        return swimmingresult.event.get_gender_display()

    def dehydrate_stroke(self, swimmingresult):
        return swimmingresult.event.get_stroke_display()


class SwimmingResultAdmin(ImportExportModelAdmin):
    resource_class = SwimmingResultResource
    fields = ['event', 'student', 'time', 'house_points']
    list_display = ('event', 'student', 'time', 'house_points')
    list_filter = ['event']
    search_fields = ['student']


class TrackRelayResultResource(resources.ModelResource):
    year_group = fields.Field(column_name='year group', attribute='event', widget=ForeignKeyWidget(Event, 'year_group'))
    event = fields.Field(column_name='distance',attribute='event')
    gender = fields.Field(column_name='gender', attribute='event', widget=ForeignKeyWidget(Event, 'gender'))
    house = fields.Field(column_name='house', attribute='house', widget=ForeignKeyWidget(House, 'house_name'))

    class Meta:
        model = TrackRelayResult
        fields = ('year_group', 'event', 'gender', 'house', 'time')
        export_order = ('year_group', 'event', 'gender', 'house', 'time')
        import_id_fields = ['event']

    def dehydrate_gender(self, trackrelayresult):
        return trackrelayresult.event.get_gender_display()

    def dehydrate_event(self, trackrelayresult):
        return '%s by %sm' % (trackrelayresult.event.number_of_students, trackrelayresult.event.distance_per_student)


class TrackRelayResultAdmin(ImportExportModelAdmin):
    resource_class = TrackRelayResultResource
    fields = ['event', 'house', 'time', 'house_points']
    list_display = ('event', 'house', 'time', 'house_points')
    list_filter = ['event']
    search_fields = ['house']


class SwimmingRelayResultResource(resources.ModelResource):
    year_group = fields.Field(column_name='year group', attribute='event', widget=ForeignKeyWidget(Event, 'year_group'))
    event = fields.Field(column_name='distance',attribute='event')
    stroke = fields.Field(column_name='stroke', attribute='event',
                          widget=ForeignKeyWidget(Event, 'stroke'))
    gender = fields.Field(column_name='gender', attribute='event', widget=ForeignKeyWidget(Event, 'gender'))
    house = fields.Field(column_name='house', attribute='house', widget=ForeignKeyWidget(House, 'house_name'))

    class Meta:
        model = SwimmingRelayResult
        fields = ('year_group', 'event', 'stroke', 'gender', 'house', 'time')
        export_order = ('year_group', 'event', 'stroke', 'gender', 'house', 'time')
        import_id_fields = ['event']

    def dehydrate_gender(self, swimmingrelayresult):
        return swimmingrelayresult.event.get_gender_display()

    def dehydrate_event(self, swimmingrelayresult):
        return '%s by %sm' % (swimmingrelayresult.event.number_of_students, swimmingrelayresult.event.distance_per_student)

    def dehydrate_stroke(self, swimmingresult):
        return swimmingresult.event.get_stroke_display()

class SwimmingRelayResultAdmin(ImportExportModelAdmin):
    resource_class = SwimmingRelayResultResource
    fields = ['event', 'house', 'time', 'house_points']
    list_display = ('event', 'house', 'time', 'house_points')
    list_filter = ['event']
    search_fields = ['house']


class TrackEventRecordAdmin(admin.ModelAdmin):
    fields = ['event', 'first_name', 'last_name', 'time']
    list_display = ('event', 'first_name', 'last_name', 'time')
    list_filter = ['event']
    search_fields = ['first_name', 'last_name']


class FieldEventRecordAdmin(admin.ModelAdmin):
    fields = ['event', 'first_name', 'last_name', 'distance']
    list_display = ('event', 'first_name', 'last_name', 'distance')
    list_filter = ['event']
    search_fields = ['first_name', 'last_name']


class TrackRelayRecordAdmin(admin.ModelAdmin):
    fields = ['event', 'house', 'time']
    list_display = ('event', 'house', 'time')
    list_filter = ['event']
    search_fields = ['house']


admin.site.register(CrossCountryResult, CrossCountryResultAdmin)
admin.site.register(TrackEventResult, TrackEventResultAdmin)
admin.site.register(FieldEventResult, FieldEventResultAdmin)
admin.site.register(SwimmingResult, SwimmingResultAdmin)
admin.site.register(TrackRelayResult, TrackRelayResultAdmin)
admin.site.register(SwimmingRelayResult, SwimmingRelayResultAdmin)
admin.site.register(TrackEventRecord, TrackEventRecordAdmin)
admin.site.register(FieldEventRecord, FieldEventRecordAdmin)
admin.site.register(TrackRelayRecord, TrackRelayRecordAdmin)
