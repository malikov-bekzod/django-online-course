from django.contrib import admin
from .models import Blog, Comment, Tag
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = [
        "title",
        "author",
    ]
    list_display_links = [
        "title",
        "author",
    ]
    search_fields = [
        "title",
        "author",
    ]


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ["text", "writer"]
    list_display_links = ["text", "writer"]
    search_fields = ["text", "writer"]


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    list_display = ["name",]
    list_display_links = ["name",]
    search_fields = ["name",]
