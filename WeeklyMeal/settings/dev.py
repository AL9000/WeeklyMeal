from .base import *

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1',)  # Used by app debug_toolbar

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
