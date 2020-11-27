"""Model classes for facts."""

import logging
import re

from django.db.models import ManyToManyField
from django.urls import reverse

from facts.models.fact_relation import (
    EntityFactRelation,
    OccurrenceFactRelation,
    TopicFactRelation,
)
from modularhistory.fields import HTMLField
from modularhistory.fields.html_field import (
    OBJECT_PLACEHOLDER_REGEX,
    TYPE_GROUP,
    PlaceholderGroups,
)
from modularhistory.utils.html import escape_quotes
from modularhistory.utils.string import dedupe_newlines, truncate
from topics.serializers import FactSerializer
from verification.models import VerifiableModel

fact_placeholder_regex = OBJECT_PLACEHOLDER_REGEX.replace(
    TYPE_GROUP, rf'(?P<{PlaceholderGroups.MODEL_NAME}>fact)'
)
logging.debug(f'Fact placeholder pattern: {fact_placeholder_regex}')


DEGREES_OF_CERTAINTY = (
    (0, 'No credible evidence'),
    (1, 'Some credible evidence'),
    (2, 'A preponderance of evidence'),
    (3, 'Beyond reasonable doubt'),
    (4, 'Beyond any shadow of a doubt'),
)


class Postulation(VerifiableModel):
    """A postulation."""

    summary = HTMLField(unique=True, paragraphed=False)
    elaboration = HTMLField(null=True, blank=True, paragraphed=True)
    supportive_facts = ManyToManyField(
        'self',
        through='facts.PostulationSupport',
        related_name='supported_facts',
        symmetrical=False,
    )
    related_entities = ManyToManyField(
        'entities.Entity', through=EntityFactRelation, related_name='facts'
    )
    related_topics = ManyToManyField(
        'topics.Topic', through=TopicFactRelation, related_name='facts'
    )
    related_occurrences = ManyToManyField(
        'occurrences.Occurrence', through=OccurrenceFactRelation, related_name='facts'
    )

    searchable_fields = ['summary', 'elaboration']
    serializer = FactSerializer

    def __str__(self) -> str:
        """Return the fact's string representation."""
        return self.summary.text

    @property
    def summary_link(self) -> str:
        """Return an HTML link to the fact, containing the summary text."""
        add_elaboration_tooltip = False
        elaboration = self.elaboration.html if self.elaboration else ''
        elaboration = elaboration.replace('\n', '')
        if add_elaboration_tooltip:
            summary_link = (
                f'<a href="{reverse("facts:detail", args=[self.pk])}" class="fact-link" '
                f'target="_blank" title="{escape_quotes(elaboration)}" '
                f'data-toggle="tooltip" data-html="true">{self.summary.html}</a>'
            )
        else:
            summary_link = (
                f'<a href="{reverse("facts:detail", args=[self.pk])}" class="fact-link" '
                f'target="_blank">{self.summary.html}</a>'
            )
        return summary_link

    @classmethod
    def get_object_html(
        cls, match: re.Match, use_preretrieved_html: bool = False
    ) -> str:
        """Return the obj's HTML based on a placeholder in the admin."""
        if not match:
            logging.error('fact.get_object_html was called without a match')
            raise ValueError
        if use_preretrieved_html:
            # Return the pre-retrieved HTML (already included in placeholder)
            preretrieved_html = match.group(PlaceholderGroups.HTML)
            if preretrieved_html:
                return preretrieved_html.strip()
        fact: 'Postulation' = cls.get_object_from_placeholder(match)
        return fact.summary_link

    @classmethod
    def get_updated_placeholder(cls, match: re.Match) -> str:
        """Return a placeholder for a model instance depicted in an HTML field."""
        placeholder = match.group(0)
        logging.debug(f'Looking at {truncate(placeholder)}')
        extant_html = match.group(PlaceholderGroups.HTML).strip()
        if extant_html:
            if '<a ' not in extant_html:
                html = cls.get_object_html(match)
                html = re.sub(
                    r'(.+?">).+?(<\/a>)',  # TODO
                    rf'\g<1>{extant_html}\g<2>',
                    html,
                )
                placeholder = placeholder.replace(
                    match.group(PlaceholderGroups.HTML), html
                )
            return placeholder
        else:
            html = cls.get_object_html(match)
            model_name = match.group(PlaceholderGroups.MODEL_NAME)
            pk = match.group(PlaceholderGroups.PK)
            placeholder = f'[[ {model_name}: {pk}: {html} ]]'
        return dedupe_newlines(placeholder)
