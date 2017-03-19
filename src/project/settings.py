# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import environ
from django.utils.translation import ugettext_lazy as _

try:
    from .settings_local import *
except ImportError:
    pass

root = environ.Path(__file__) - 1
env = environ.Env(DEBUG=(bool, False),)

environ.Env.read_env(
    os.path.join(str(environ.Path(__file__) - 2), '.env')
)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = root()

os.environ.setdefault('BASE_DIR', BASE_DIR)

os.sys.path.insert(0, os.path.join(PROJECT_DIR))
os.sys.path.insert(0, os.path.join(PROJECT_DIR, 'apps'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS').split(',')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'redactor',
    'easy_thumbnails',
    'solo',
    'compressor',
    'bootstrap3',
    'robots',
    'admin_honeypot',
    'django_extensions',

    'apps.common',
)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {'default': env.db()}

USE_TZ = True
TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'ru'
LANGUAGES = [
    ('ru', _('Russian')),
]

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_URL = '/media/'
MEDIA_ROOT = (root - 1)('media')

STATIC_URL = '/static/'
STATIC_ROOT = (root - 1)('static')

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

COMPRESS_ENABLED = not DEBUG
COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_OUTPUT_DIR = 'CACHE'

EMAIL_CONFIG = env.email_url(
    'EMAIL_URL',
    default='smtp://localhost:25'
)

BASE_URL = env('BASE_URL')

ROBOTS_USE_SITEMAP = True
ROBOTS_SITEMAP_URLS = [
    '{}/sitemap.xml'.format(BASE_URL),
]

try:
    from .settings_local import *
except ImportError:
    pass
