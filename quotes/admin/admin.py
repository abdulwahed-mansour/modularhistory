from admin import admin_site, Admin, TabularInline
from occurrences.models import Occurrence
from sources.admin.citations import CitationsInline
from topics.models import TopicQuoteRelation
from .filters import (
    TopicFilter,
    AttributeeFilter,
    # AttributeeClassificationFilter,
    HasSourceFilter,
    AttributeeCountFilter,
    HasMultipleCitationsFilter
)
from .. import models


class OccurrencesInline(TabularInline):
    model = Occurrence.related_quotes.through
    autocomplete_fields = ['occurrence']

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.related_occurrences.count():
            return 0
        return 1


class TopicsInline(TabularInline):
    model = TopicQuoteRelation
    extra = 1
    autocomplete_fields = ['topic']


class AttributeesInline(TabularInline):
    model = models.QuoteAttribution
    autocomplete_fields = ['attributee']

    sortable_field_name = 'position'

    def get_extra(self, request, obj=None, **kwargs):
        if obj and obj.attributees.count():
            return 0
        return 1


class BitesInline(TabularInline):
    model = models.QuoteBite
    extra = 0


# class QuoteForm(ModelForm):
#     fields = []
#
#     class Meta:
#         model = models.Quote


class QuoteAdmin(Admin):
    # form = QuoteForm
    list_display = [
        'bite',
        'detail_link',
        'attributee_html',
        'date_string',
        'citation_html',
        'related_topics_string'
    ]
    list_filter = [
        'verified',
        HasSourceFilter,
        HasMultipleCitationsFilter,
        TopicFilter,
        AttributeeFilter,
        AttributeeCountFilter,
        # AttributeeClassificationFilter  # broken
        '_attributee__classifications',
        'attributees__classifications'
    ]
    search_fields = models.Quote.searchable_fields
    ordering = ('date', '_attributee')
    autocomplete_fields = ['_attributee']
    readonly_fields = ['citation_html']
    inlines = [
        AttributeesInline,
        CitationsInline,
        OccurrencesInline,
        TopicsInline,
        BitesInline
    ]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        for field_name in ('date', 'date_is_circa'):
            if fields and field_name in fields:
                fields.remove(field_name)
                fields.append(field_name)
        return fields


admin_site.register(models.Quote, QuoteAdmin)