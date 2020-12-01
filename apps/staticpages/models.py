from django.contrib.flatpages.models import FlatPage
from django.db import models

META_DESCRIPTION_MAX_LENGTH: int = 200


class AbstractFlatPage(FlatPage):
    """TODO: write docstring."""

    class Meta:
        abstract = True


class StaticPage(AbstractFlatPage):
    """TODO: write docstring."""

    meta_description = models.TextField(max_length=META_DESCRIPTION_MAX_LENGTH)

    class Meta:
        ordering = ['url']