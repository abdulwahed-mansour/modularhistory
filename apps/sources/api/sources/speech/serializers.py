from apps.propositions.api.serializers import PropositionDrfSerializer
from apps.sources.api.serializers import SourceDrfSerializer
from apps.sources.models import Speech


class SpeechDrfSerializer(SourceDrfSerializer):
    """Serializer for speech sources."""

    utterance_serialized = PropositionDrfSerializer(read_only=True, source='utterance')

    class Meta(SourceDrfSerializer.Meta):
        model = Speech
        fields = SourceDrfSerializer.Meta.fields + [
            'type',
            'audience',
            'utterance',
            'utterance_serialized',
        ]
