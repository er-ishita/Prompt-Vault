from django.contrib import admin

from .models import Prompt


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "category", "visibility", "view_count", "created_at")
    list_filter = ("visibility", "category")
    search_fields = ("title", "description", "creator__username")
    filter_horizontal = ("tags",)
