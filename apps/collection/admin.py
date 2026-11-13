from django.contrib import admin

from .models import Collection, CollectionItem


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "is_public", "created_at")
    list_filter = ("is_public",)
    search_fields = ("name", "description", "owner__username")


@admin.register(CollectionItem)
class CollectionItemAdmin(admin.ModelAdmin):
    list_display = ("collection", "prompt", "added_at")
    search_fields = ("collection__name", "prompt__title")
