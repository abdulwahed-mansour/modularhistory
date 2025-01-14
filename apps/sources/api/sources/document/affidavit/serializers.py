from apps.sources.api.serializers import DocumentDrfSerializerMixin, SourceDrfSerializer
from apps.sources.models import Affidavit


class _AffidavitDrfSerializer(SourceDrfSerializer, DocumentDrfSerializerMixin):
    """Serializer for affidavit document sources."""

    class Meta(SourceDrfSerializer.Meta):
        location_required = True
        model = Affidavit
        fields = (
            SourceDrfSerializer.Meta.fields
            + DocumentDrfSerializerMixin.Meta.fields
            + ['certifier']
        )
        extra_kwargs = SourceDrfSerializer.Meta.extra_kwargs | {
            'location': {'required': True, 'write_only': True}
        }


class AffidavitDrfSerializer(_AffidavitDrfSerializer):
    """Serializer for affidavit document sources."""

    originalEdition = _AffidavitDrfSerializer(read_only=True, source='original_edition')
