from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

THIRD_PARTY_APPS += ('debug_toolbar',)

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

MIDDLEWARE.insert(3, 'debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
