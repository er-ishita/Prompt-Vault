from django.db import models
from django.conf import settings

from apps.taxonomy.models import Category, Tag


class Prompt(models.Model):

    VISIBILITY_CHOICES = [
        ("public", "Public"),
        ("private", "Private"),
        ("unlisted", "Unlisted"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    content = models.TextField()

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="prompts"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prompts"
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="prompts"
    )

    visibility = models.CharField(
        max_length=10,
        choices=VISIBILITY_CHOICES,
        default="public"
    )

    view_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["visibility", "-created_at"]),
        ]

    def __str__(self):
        return self.title