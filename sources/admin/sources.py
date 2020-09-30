from typing import List

from admin.admin import (Admin, GenericTabularInline, StackedInline, TabularInline, admin_site)
from sources import models
from sources.admin.source_filters import (
    HasContainerFilter,
    HasFileFilter,
    HasFilePageOffsetFilter,
    HasPageNumber,
    ImpreciseDateFilter,
    TypeFilter
)


class AttributeesInline(TabularInline):
    """TODO: add docstring."""

    model = models.Source.attributees.through
    autocomplete_fields = ['attributee']

    # https://django-grappelli.readthedocs.io/en/latest/customization.html#inline-sortables
    sortable_field_name = 'position'

    def get_extra(self, request, obj=None, **kwargs):
        """TODO: add docstring."""
        if obj and obj.attributees.count():
            return 0
        return 1


class ContainersInline(TabularInline):
    """TODO: add docstring."""

    verbose_name = 'container'
    verbose_name_plural = 'containers'
    model = models.Source.containers.through
    fk_name = 'source'
    extra = 0
    autocomplete_fields = ['container']


class ContainedSourcesInline(TabularInline):
    """TODO: add docstring."""

    verbose_name = 'contained source'
    verbose_name_plural = 'contained sources'
    model = models.Source.containers.through
    fk_name = 'container'
    extra = 0
    autocomplete_fields = ['source']


class RelatedInline(GenericTabularInline):
    """TODO: add docstring."""

    model = models.Citation
    extra = 0
    verbose_name = 'related obj'
    verbose_name_plural = 'related objects (not yet implemented)'

    # https://django-grappelli.readthedocs.io/en/latest/customization.html#inline-sortables
    sortable_field_name = 'position'


class SourceAdmin(Admin):
    """TODO: add docstring."""

    model = models.Source
    list_display = [
        'pk',
        'html',
        'date_string',
        'location',
        'admin_file_link'
    ]
    list_filter = [
        'verified',
        HasContainerFilter,
        HasFileFilter,
        HasFilePageOffsetFilter,
        HasPageNumber,
        ImpreciseDateFilter,
        'hidden',
        'attributees',
        TypeFilter
    ]
    readonly_fields = ['db_string']
    search_fields = models.Source.searchable_fields
    ordering = ['date', 'db_string']
    inlines = [AttributeesInline, ContainersInline, ContainedSourcesInline, RelatedInline]
    autocomplete_fields = ['db_file', 'location']

    def get_fields(self, request, obj=None):
        """TODO: add docstring."""
        fields = list(super().get_fields(request, obj))
        if 'database_string' in fields:
            fields.remove('database_string')
            fields.insert(0, 'database_string')
        return fields


class ChildModelAdmin(SourceAdmin):
    """TODO: add docstring."""

    list_display = [
        'pk',
        'html',
        'detail_link',
        'date_string'
    ]
    list_filter = ['verified', 'attributees']
    readonly_fields = ['db_string']
    search_fields = ['db_string']
    ordering = ['date', 'db_string']
    # inlines = SourceAdmin.inlines
    # autocomplete_fields = SourceAdmin.autocomplete_fields

    def get_fields(self, request, obj=None):
        """TODO: add docstring."""
        fields: List = list(super().get_fields(request, obj))
        # Fields to display at the top, in order
        top_fields = (
            'db_string',
            'creators',
            'title'
        )
        # Fields to display at the bottom, in order
        bottom_fields = (
            'volume',
            'number',
            'page_number',
            'end_page_number',
            'container',
            'description',
            'citations'
        )
        index: int = 0
        for field_name in top_fields:
            if field_name in fields:
                fields.remove(field_name)
                fields.insert(index, field_name)
                index += 1
        for field_name in bottom_fields:
            if field_name in fields:
                fields.remove(field_name)
                fields.append(field_name)
        return fields


class PublicationAdmin(Admin):
    """TODO: add docstring."""

    list_display = ['__str__', 'description']
    search_fields = ['name']


class ArticleAdmin(ChildModelAdmin):
    """TODO: add docstring."""

    list_display = ['pk', 'html', 'publication', 'description', 'date_string']
    autocomplete_fields = ChildModelAdmin.autocomplete_fields + ['publication']
    ordering = ChildModelAdmin.ordering


class BookAdmin(ChildModelAdmin):
    """TODO: add docstring."""

    list_display = ChildModelAdmin.list_display
    autocomplete_fields = ChildModelAdmin.autocomplete_fields + ['original_edition']
    ordering = ChildModelAdmin.ordering


class ArticlesInline(StackedInline):
    """TODO: add docstring."""

    model = models.Article
    extra = 1


class SpeechAdmin(ChildModelAdmin):
    """TODO: add docstring."""

    list_display = ['string', 'location', 'date_string']
    search_fields = ['db_string', 'location__name']


class CollectionAdmin(Admin):
    """TODO: add docstring."""

    search_fields = ['name', 'repository__name', 'repository__location__name']
    autocomplete_fields = ['repository']


class DocumentAdmin(ChildModelAdmin):
    """TODO: add docstring."""

    search_fields = ChildModelAdmin.search_fields
    autocomplete_fields = ['collection', 'db_file']


class RepositoryAdmin(Admin):
    """TODO: add docstring."""

    search_fields = ['name', 'location__name']
    autocomplete_fields = ['location']


class SourcesInline(TabularInline):
    """TODO: add docstring."""

    model = models.Source
    extra = 0
    fields = ['verified', 'hidden', 'date_is_circa', 'creators', 'url', 'date', 'publication_date']


admin_site.register(models.Source, SourceAdmin)

admin_site.register(models.Article, ArticleAdmin)
admin_site.register(models.Book, BookAdmin)
admin_site.register(models.Speech, SpeechAdmin)

admin_site.register(models.Publication, PublicationAdmin)

admin_site.register(models.Document, DocumentAdmin)
admin_site.register(models.Letter, DocumentAdmin)
admin_site.register(models.Collection, CollectionAdmin)
admin_site.register(models.Repository, RepositoryAdmin)

admin_site.register(models.JournalEntry, ChildModelAdmin)

child_models = (
    models.Chapter,
    models.Interview,
    models.Piece,
    models.Documentary,
    models.WebPage,
    models.Affidavit
)

for child in child_models:
    admin_site.register(child, ChildModelAdmin)