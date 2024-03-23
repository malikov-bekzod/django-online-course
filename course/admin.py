from django.contrib import admin
from .models import Course,Category
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    list_display = ["title", "description", "price", "student_count"]
    list_display_links = ["title", "description", "price", "student_count"]
    search_fields = ["title","description"]


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ["name", "description","course_count"]
    list_display_links = ["name", "description","course_count"]
    search_fields = ["name", "description","course_count"]
