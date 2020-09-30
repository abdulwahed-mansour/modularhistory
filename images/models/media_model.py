from django.db import models

from history.fields import HTMLField
from history.models import DatedModel, SearchableModel

PROVIDER_MAX_LENGTH: int = 200


class MediaModel(DatedModel, SearchableModel):
    """TODO: add docstring."""

    caption = HTMLField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    provider = models.CharField(
        max_length=PROVIDER_MAX_LENGTH,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True