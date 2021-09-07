import pytest
from django.conf import settings
from django.contrib.sites.models import Site
from django.urls import reverse
from rest_framework.test import APIClient

from apps.flatpages.models import FlatPage
from apps.redirects.models import Redirect


@pytest.fixture()
def api_client():
    """Return an API client to be used in a test."""
    return APIClient()


@pytest.mark.django_db()
class TestFlatPages:
    """Test the flatpages app."""

    def test_changing_flatpage_path(self, api_client: APIClient):
        """
        Test adding a new flatpage and then changing its path.

        When the flatpage's path is changed, a redirect should be created
        from the page's prior path to its new path.
        """
        original_path = '/flatpage/'
        original_url = reverse('flatpages_api:flatpage', kwargs={'path': original_path})
        new_path = '/newpath/'
        new_url = reverse('flatpages_api:flatpage', kwargs={'path': new_path})

        # Create the flatpage.
        flatpage: FlatPage = FlatPage.objects.create(
            title='Flat Page',
            content='<p>This is a flat page.</p>',
            path=original_path,
            verified=True,
        )
        flatpage.sites.add(Site.objects.get(pk=settings.SITE_ID))

        # Confirm the flatpage can be retrieved by its path.
        assert FlatPage.objects.filter(path=original_path).exists()
        response = api_client.get(original_url)
        assert response.status_code == 200

        # Change the flatpage's path.
        flatpage.path = new_path
        flatpage.save()

        # Confirm the flatpage can be retrieved by its new path.
        response = api_client.get(new_url)
        assert response.status_code == 200

        # Confirm a redirect was created.
        assert Redirect.objects.filter(old_path=original_path, new_path=new_path).exists()