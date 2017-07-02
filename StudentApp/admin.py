from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from .models import *


class HouseInline(admin.TabularInline):
    model = House
    extra = 0


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


class SchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('school_name',)}
    fields = ['school_name', 'school_location', 'slug']
    list_display = ('school_name', 'school_location')
    inlines = [HouseInline]


class HouseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('house_name',)}
    fields = ['house_name', 'slug']
    inlines = [StudentInline]


class StudentResource(resources.ModelResource):
    house = fields.Field(column_name='house', attribute='house', widget=ForeignKeyWidget(House, 'house_name'))

    class Meta:
        model = Student
        fields = ('house', 'first_name', 'last_name', 'gender', 'year_group')
        export_order = ('year_group', 'house', 'gender', 'last_name', 'first_name')
        import_id_fields = ['first_name', 'last_name']


class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource


admin.site.register(School, SchoolAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Student, StudentAdmin)
