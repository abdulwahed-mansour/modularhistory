import re
from sys import stderr

from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

from history.fields.html_field import entity_name_regex

register = template.Library()


@register.filter(is_safe=True)
def with_entity_links(value: str):
    html = value
    if re.search(entity_name_regex, html):
        # from entities.models import Entity
        processed_entity_keys = []
        for match in re.finditer(entity_name_regex, html):
            key = match.group(1).strip()
            entity_name = match.group(2)
            # Process the entity name if it hasn't already been processed
            if key not in processed_entity_keys:
                processed_entity_keys.append(key)
                try:
                    # entity = Entity.objects.get(pk=key)
                    entity_link = (f'<a href="{reverse("entities:detail", args=[key])}" '
                                   f'target="_blank">{entity_name}</a>')
                    html = html.replace(match.group(0), entity_link, 1)
                except Exception as e:
                    print(f'{e}', file=stderr)
    return mark_safe(html)