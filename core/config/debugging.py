"""Settings for debugging."""

import re

from core.environment import TESTING

# https://docs.djangoproject.com/en/dev/ref/settings#s-internal-ips
INTERNAL_IPS = ['127.0.0.1', '172.27.0.5']

# https://github.com/jazzband/django-silk
SILKY_PYTHON_PROFILER = True
SILKY_ANALYZE_QUERIES = True
SILKY_AUTHENTICATION = True  # User must login.
SILKY_AUTHORISATION = True  # User must have permissions.
SILKY_PERMISSIONS = lambda user: user.is_superuser

PROFILE_ALL_REQUESTS = True


def intercept(request) -> bool:
    """Determine whether to intercept a request for profiling."""
    qualifiers = (PROFILE_ALL_REQUESTS or request.user.is_superuser,)
    disqualifiers = (
        TESTING,
        re.search(r'(?:healthcheck)/', request.path),
    )
    if any(qualifiers) and not any(disqualifiers):
        return True
    return False


SILKY_INTERCEPT_FUNC = intercept
