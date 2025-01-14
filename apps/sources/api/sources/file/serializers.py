from apps.sources.models import SourceFile
from core.models.model import DrfModelSerializer


class SourceFileDrfSerializer(DrfModelSerializer):
    """Serializer for sources files."""

    class Meta(DrfModelSerializer.Meta):
        model = SourceFile
        fields = DrfModelSerializer.Meta.fields + [
            'file',
            'name',
            'page_offset',
            'first_page_number',
            'uploaded_at',
        ]
        read_only_fields = ['uploaded_at']
        extra_kwargs = {'file': {'required': True}}
