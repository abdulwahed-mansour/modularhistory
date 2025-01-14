from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl.registries import registry

from apps.entities.models.entity import Entity
from apps.search.documents.config import (
    DEFAULT_INDEX_SETTINGS,
    html_field_analyzer,
    instant_search_analyzer,
)

from .base import Document


@registry.register_document
class EntityDocument(Document):
    """ElasticSearch document for entities."""

    class Index:
        settings = DEFAULT_INDEX_SETTINGS
        name = 'entities'

    name = fields.TextField()
    aliases = fields.TextField()
    description = fields.TextField(analyzer=html_field_analyzer)

    class Django:
        model = Entity


@registry.register_document
class EntityInstantSearchDocument(Document):
    """ElasticSearch document for entities used by search-as-you-type."""

    class Index:
        settings = DEFAULT_INDEX_SETTINGS
        name = 'entities_instant_search'

    name = fields.TextField(analyzer=instant_search_analyzer)
    aliases = fields.TextField(analyzer=instant_search_analyzer)

    class Django:
        model = Entity
