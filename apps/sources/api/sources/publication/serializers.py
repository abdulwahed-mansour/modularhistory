from rest_framework import serializers

from apps.dates.fields import HistoricDateTimeDrfField
from apps.sources.api.serializers import SourceDrfSerializer, TextualDrfSerializerMixin
from apps.sources.models import Webpage, Website
from apps.sources.models.publication import AbstractPublication, Publication
from core.models.model import DrfModelSerializer, DrfTypedModelSerializer


class PublicationDrfMixinSerializer(serializers.ModelSerializer):
    """Serializer for abstract publication sources."""

    class Meta:
        model = AbstractPublication
        fields = ['name', 'aliases', 'description']


class PublicationDrfSerializer(DrfTypedModelSerializer, PublicationDrfMixinSerializer):
    """Serializer for publication sources."""

    class Meta(SourceDrfSerializer.Meta):
        model = Publication
        fields = (
            DrfTypedModelSerializer.Meta.fields + PublicationDrfMixinSerializer.Meta.fields
        )


class _WebpageDrfSerializer(SourceDrfSerializer, TextualDrfSerializerMixin):
    """Serializer for webpage sources."""

    date = HistoricDateTimeDrfField(write_only=True, required=False)

    def validate(self, attrs):
        if not attrs.get('website') and not attrs.get('website_name'):
            raise serializers.ValidationError(
                'Please specify either `website` or `website_name`.'
            )
        return attrs

    class Meta(SourceDrfSerializer.Meta):
        model = Webpage
        fields = (
            SourceDrfSerializer.Meta.fields
            + TextualDrfSerializerMixin.Meta.fields
            + [
                'website_name',
                'website',
            ]
        )


class WebpageDrfSerializer(_WebpageDrfSerializer):
    """Serializer for webpage sources."""

    originalEdition = _WebpageDrfSerializer(read_only=True, source='original_edition')


class WebsiteDrfSerializer(DrfModelSerializer, PublicationDrfMixinSerializer):
    """Serializer for website sources."""

    class Meta(DrfModelSerializer.Meta):
        model = Website
        fields = (
            DrfModelSerializer.Meta.fields
            + PublicationDrfMixinSerializer.Meta.fields
            + ['owner']
        )
