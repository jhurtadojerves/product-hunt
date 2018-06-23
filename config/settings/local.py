from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

THIRD_PARTY_APPS += ('django_debug_toolbar',)

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
