import os
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting


class LocalArtifactsStorage(FileSystemStorage):
    """Storage class for artifacts stored in the local filesystem."""

    location = setting('ARTIFACTS_ROOT')
    base_url = setting('ARTIFACTS_URL')

    def __init__(self, *args, **kwargs):
        """Instantiate LocalArtifactsStorage."""
        if not os.path.exists(self.location):
            # TODO: Make sure this does not break if writing permissions are missing
            os.makedirs(self.location)
        super().__init__(*args, **kwargs)


class GoogleCloudArtifactsStorage(GoogleCloudStorage):
    """Storage class for artifacts stored in Google Cloud Storage."""

    bucket_name = setting('GS_ARTIFACTS_BUCKET_NAME')

    def url(self, name):
        """Give the correct artifact URL (not the Google-generated url)."""
        return urljoin(settings.ARTIFACTS_URL, name)


class GoogleCloudMediaFileStorage(GoogleCloudStorage):
    """Storage class for media files stored in Google Cloud Storage."""

    bucket_name = setting('GS_MEDIA_BUCKET_NAME')
    location = 'media'

    def url(self, name):
        """Give the correct media URL (not the Google-generated url)."""
        return urljoin(settings.MEDIA_URL, name)


# TODO
class GoogleCloudStaticFileStorage(GoogleCloudStorage):
    """Storage class for static files stored in Google Cloud Storage."""

    bucket_name = setting('GS_STATIC_BUCKET_NAME')

    def url(self, name):
        """Give the correct static URL (not the Google-generated URL)."""
        return urljoin(settings.STATIC_URL, name)