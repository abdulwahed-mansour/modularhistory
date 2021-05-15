from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl.registries import registry

from apps.entities.models.entity import Entity
from apps.quotes.models.quote import Quote
from apps.search.documents.config import (
    DEFAULT_INDEX_SETTINGS,
    get_index_name_for_ct,
    html_field_analyzer,
)
from apps.sources.models.source import Source
from core.constants.content_types import ContentTypes

from .base import Document


@registry.register_document
class QuoteDocument(Document):
    class Index:
        settings = DEFAULT_INDEX_SETTINGS
        name = get_index_name_for_ct(ContentTypes.quote)

    text = fields.TextField(attr='text.raw_value', analyzer=html_field_analyzer)
    context = fields.TextField(attr='context.raw_value', analyzer=html_field_analyzer)
    attributees = fields.ObjectField(
        properties={
            'id': fields.IntegerField(),
            'name': fields.TextField(),
            'aliases': fields.TextField(),
            'description': fields.TextField(attr='description.raw_value'),
        }
    )
    citations = fields.TextField(attr='citation_html', analyzer=html_field_analyzer)
    topics = fields.ObjectField(
        attr='_related_topics',
        properties={
            'id': fields.IntegerField(),
            'key': fields.TextField(),
            'aliases': fields.TextField(),
            'description': fields.TextField(
                attr='description.raw_value', analyzer=html_field_analyzer
            ),
            'path': fields.TextField(),
        },
    )

    class Django:
        model = Quote
        related_models = [Source, Entity]

    def get_queryset(self):
        return (
            super().get_queryset().prefetch_related('attributees', 'sources', 'topics')
        )