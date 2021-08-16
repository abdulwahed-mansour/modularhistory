import pytest
from django.contrib.contenttypes.models import ContentType

from apps.dates.structures import HistoricDateTime
from apps.moderation.models.change import Change
from apps.propositions.models import Proposition


@pytest.mark.django_db()
class TestModeration:
    """Test the moderation app."""

    def test_making_a_change(self):
        """Test making a change to a moderated model instance."""
        original_summary = 'summary'
        changed_summary = 'changed summary'

        # Create and save a model instance.
        p = Proposition(
            type='propositions.conclusion',
            summary=original_summary,
            elaboration='<p>elaboration</p>',
            certainty=1,
            date=HistoricDateTime(2000, 1, 1, 1, 1, 1, microsecond=1),
        )
        p.save()

        # Create and save a `Change` instance in which a field is modified.
        p.summary = changed_summary
        change = Change(
            content_type=ContentType.objects.get_for_model(Proposition),
            object_id=p.pk,
            changed_object=p,
        )
        assert change.changed_object.summary == changed_summary
        change.save()

        # Modify another field.
        changed_title = 'changed title'
        change.changed_object.title = changed_title
        change.save()

        # Verify the change state is separate from the model instance state.
        change.refresh_from_db()
        p.refresh_from_db()
        assert change.changed_object.summary == changed_summary
        assert p.summary == original_summary
        assert change.changed_object.title == changed_title
        assert change.changed_object.title != p.title
        assert change.changed_object.date == change.content_object.date