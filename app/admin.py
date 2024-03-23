from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
# Register your models here.

@admin.register(Avto)
class AvtoAdmin(admin.ModelAdmin):
    list_display = ("id", "brend", "model", "size", "layer", "price", "sizes", )
    list_display_links = ("id", "brend", "model",  "size", "layer", "price", "sizes", )
    search_fields = ("brend","model", "size", )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ("id", "name", )
    search_fields = ("name", )
    

@admin.register(SizeCategory)
class SizeCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "differens", )
    list_display_links = ("id", "differens", )

@admin.register(Conferens)
class SizeCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "bio", )
    list_display_links = ("id", "bio", )


@admin.register(Cart)
class KarzinkaAdmin(admin.ModelAdmin):
    list_display = ("id",)
    list_display_links = ["id"]