from django.db import models
from django.conf import settings

from apps.prompts.models import Prompt


class Collection(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="collections"
    )

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.owner.username}"


class CollectionItem(models.Model):

    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name="items"
    )

    prompt = models.ForeignKey(
        Prompt,
        on_delete=models.CASCADE,
        related_name="collection_items"
    )

    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["collection", "prompt"],
                name="unique_prompt_per_collection"
            )
        ]

    def __str__(self):
        return f"{self.prompt.title} in {self.collection.name}"