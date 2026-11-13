from django.contrib import admin

from .models import Bookmark, Review


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "prompt", "created_at")
    search_fields = ("user__username", "prompt__title")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "prompt", "rating", "created_at")
    list_filter = ("rating",)
    search_fields = ("user__username", "prompt__title", "comment")
