import logging
from typing import Dict, Optional

from django.forms import ModelForm
from django.urls import path

from admin import SearchableModelAdmin, TabularInline, admin_site
from entities.views import EntitySearchView
from sources import models
from sources.admin.filters import (
    AttributeeFilter,
    HasContainerFilter,
    HasFileFilter,
    HasFilePageOffsetFilter,
    ImpreciseDateFilter,
    TypeFilter,
)
from sources.admin.source_inlines import (
    AttributeesInline,
    ContainedSourcesInline,
    ContainersInline,
    RelatedInline,
)

INITIAL = 'initial'


class SourceForm(ModelForm):
    """Form for adding/editing sources."""

    model = models.Source

    class Meta:
        model = models.Source
        exclude = model.inapplicable_fields

    def __init__(self, *args, **kwargs):
        """Construct the source form."""
        instance: Optional[models.Source] = kwargs.get('instance', None)
        schema: Dict = instance.extra_fields if instance else self.model.extra_fields
        initial = kwargs.pop(INITIAL, {})
        if instance is None:
            source_type = f'sources.{self.model.__name__.lower()}'
            logging.info(f'Setting initial type to {source_type}')
            initial['type'] = source_type
        if schema:
            initial_extra_fields = initial.get(self.model.FieldNames.extra, {})
            for key in schema:
                initial_value = instance.extra.get(key, None) if instance else None
                initial_extra_fields[key] = initial_value
            initial[models.Source.FieldNames.extra] = initial_extra_fields
        kwargs[INITIAL] = initial
        super().__init__(*args, **kwargs)


class SourceAdmin(SearchableModelAdmin):
    """Admin for sources."""

    model = models.Source
    form = SourceForm
    list_display = [
        model.FieldNames.pk,
        'html',
        'date_string',
        model.FieldNames.location,
        'admin_source_link',
        'type',
    ]
    list_filter = [
        model.FieldNames.verified,
        HasContainerFilter,
        HasFileFilter,
        HasFilePageOffsetFilter,
        ImpreciseDateFilter,
        model.FieldNames.hidden,
        AttributeeFilter,
        TypeFilter,
    ]
    readonly_fields = SearchableModelAdmin.readonly_fields + [
        model.FieldNames.string,
    ]
    search_fields = models.Source.searchable_fields
    ordering = ['date', model.FieldNames.string]
    inlines = [
        AttributeesInline,
        ContainersInline,
        ContainedSourcesInline,
        RelatedInline,
    ]
    autocomplete_fields = [model.FieldNames.file, model.FieldNames.location]

    # https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_per_page
    list_per_page = 10

    # https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_as
    save_as = True

    # https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_as_continue
    save_as_continue = True

    def get_queryset(self, request):
        """
        Return the queryset of quotes to be displayed in the admin.

        https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_queryset
        """
        qs = models.Source.objects.all().select_related(
            models.Source.FieldNames.file,
            models.Source.FieldNames.location,
        )
        ordering = self.get_ordering(request)
        if ordering and ordering != models.Source.get_meta().ordering:
            qs = qs.order_by(*ordering)
        return qs

    def get_fields(self, request, model_instance=None):
        """Return reordered fields to be displayed in the admin."""
        fields = list(super().get_fields(request, model_instance))
        fields_to_move = (models.Source.FieldNames.string,)
        for field in fields_to_move:
            if field in fields:
                fields.remove(field)
                fields.insert(0, field)
        return fields

    def get_urls(self):
        """TODO: add docstring."""
        urls = super().get_urls()
        additional_urls = [
            path(
                'entity_search/',
                self.admin_site.admin_view(EntitySearchView.as_view(model_admin=self)),
                name='entity_search',
            ),
        ]
        return additional_urls + urls


class SpeechForm(SourceForm):
    """Form for adding/editing speeches."""

    model = models.Speech


class SpeechAdmin(SourceAdmin):
    """Admin for speeches."""

    model = models.Speech
    form = SpeechForm
    list_display = ['string', model.FieldNames.location, 'date_string']
    search_fields = [model.FieldNames.string, 'location__name']


class SourcesInline(TabularInline):
    """Inline admin for sources."""

    model = models.Source
    extra = 0
    fields = [
        'verified',
        'hidden',
        'date_is_circa',
        'creators',
        model.FieldNames.url,
        'date',
        'publication_date',
    ]


admin_site.register(models.Source, SourceAdmin)
admin_site.register(models.Documentary, SourceAdmin)
admin_site.register(models.Speech, SpeechAdmin)
admin_site.register(models.Interview, SpeechAdmin)