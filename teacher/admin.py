from django.contrib import admin
from .models import Teacher, Speciality
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Teacher)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = [
        "first_name",
        "last_name",
    ]
    list_display_links = [
        "first_name",
        "last_name",
    ]
    search_fields = [
        "first_name",
        "last_name",
    ]


@admin.register(Speciality)
class SpecialityAdmin(ImportExportModelAdmin):
    list_display = [
        "name",
    ]
    list_display_links = [
        "name",
    ]
    search_fields = [
        "name",
    ]
