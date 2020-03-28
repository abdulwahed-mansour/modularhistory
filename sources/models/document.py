from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.utils.safestring import SafeText, mark_safe

from history.models import Model
from .base import TitleMixin, TextualSource, _Piece


class DocumentMixin(Model):
    collection = ForeignKey('Collection', related_name='%(class)s', null=True, blank=True, on_delete=CASCADE)
    collection_number = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text='aka acquisition number'
    )
    location_info = models.CharField(
        max_length=400, null=True, blank=True,
        help_text='Ex: John H. Alexander Papers, Series 1: Correspondence, 1831-1848, Folder 1'
    )

    HISTORICAL_ITEM_TYPE = 'writing'

    class Meta:
        abstract = True


class _Document(DocumentMixin, TextualSource):
    collection = ForeignKey('Collection', related_name='%(class)s', null=True, blank=True, on_delete=CASCADE)
    collection_number = models.PositiveSmallIntegerField(
        null=True, blank=True,
        help_text='aka acquisition number'
    )
    location_info = models.CharField(
        max_length=400, null=True, blank=True,
        help_text='Ex: John H. Alexander Papers, Series 1: Correspondence, 1831-1848, Folder 1'
    )
    information_url = models.URLField(
        max_length=100, null=True, blank=True,
        help_text='URL for information regarding the document'
    )

    HISTORICAL_ITEM_TYPE = 'writing'

    class Meta:
        abstract = True


class Collection(Model):
    name = models.CharField(max_length=100, help_text='e.g., "Adam S. Bennion papers"', null=True, blank=True)
    repository = ForeignKey('Repository', on_delete=CASCADE, help_text='the collecting institution')
    link = models.URLField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ['name', 'repository']

    def __str__(self):
        string = ''
        if self.name:
            string += f'{self.name}' if self.name else ''
            string += ', ' if self.repository else ''
        string += f'{self.repository}' if self.repository else ''
        return string


class Repository(Model):
    name = models.CharField(max_length=100, null=True, blank=True,
                            help_text='e.g., "L. Tom Perry Special Collections"')
    owner = models.CharField(max_length=100, null=True, blank=True,
                             help_text='e.g., "Harold B. Lee Library, Brigham Young University"')
    location = ForeignKey('places.Place', on_delete=models.SET_NULL,
                          related_name='repositories', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Repositories'

    def __str__(self):
        string = self.name
        if self.owner:
            string += f', {self.owner}'
        if self.location:
            string += f', {self.location.string}'
        return string


class Document(TitleMixin, _Document):
    def __str__(self) -> SafeText:
        string = ''
        string += f'{self.attributee_string}, ' if self.attributee_string else ''
        string += f'"{self.title}," ' if self.title else 'untitled document, '
        string += f'{self.date.string}' if self.date else 'date unknown'
        string += f', archived in {self.collection}' if self.collection else ''
        return mark_safe(string)


letter_types = (
    ('email', 'email'),
    ('letter', 'letter'),
    ('memorandum', 'memorandum'),
)


class Letter(_Document):
    recipient = models.CharField(max_length=100, null=True, blank=True)
    type2 = models.CharField(max_length=10, choices=letter_types, default='letter')

    class Meta:
        verbose_name = 'correspondence'
        verbose_name_plural = 'correspondence'

    def __str__(self) -> SafeText:
        string = f'{self.attributee_string}, letter to {self.recipient or "<Unknown>"}'
        if self.date:
            string += ', dated ' if self.date.day_is_known else ', '
            string += self.date.string
        if self.collection:
            string += f', archived in {self.collection}'
        # elif self.container:
        #     containment = self.source_containments.get(container=self.container)
        #     string += f', '
        #     string += f'{containment.phrase} ' or ''
        #     string += f'in {self.container}'
        return mark_safe(string)


class Affidavit(_Document):
    certifier = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        string = f'{self.attributee_string}, '
        string += f'affidavit sworn {self.date_html} at {self.location} before {self.certifier}'
        return mark_safe(string)

    def clean(self):
        super().clean()
        if not self.location:
            raise ValidationError('Affidavit needs a certification location.')


class JournalEntry(_Piece):

    class Meta:
        verbose_name_plural = 'Journal entries'

    def __str__(self) -> SafeText:
        string = f'{self.attributee_string}, journal ' if self.attributee_string else 'Journal '
        string += f'entry dated {self.date.string}' if self.date else ''
        return mark_safe(string)
