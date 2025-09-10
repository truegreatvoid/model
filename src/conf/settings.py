import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
APPS_DEPENDENCIES = [
    'django_extensions',
    'simple_history',
    'drf_spectacular',
    'rest_framework',
    'rest_framework_tracking',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'corsheaders',
    'channels',
]
APPS_LIST_PACKAGES = [
    'model_apps.core',
    'model_apps.organization',
    'model_apps.customer',
    'model_apps.billing',
    'model_apps.position',
    'model_apps.client',
    'model_apps.setting',
    'model_apps.webhook',
    'model_apps.websocket',
    'model_apps.permission',
    'model_apps.department',
    'model_apps.serializer',
    'model_apps.authentication',
    'model_apps.mixin',
    'model_apps.service',
    'model_apps.util',
]
APPS_LIST = [
    'apps.docs',
]

INSTALLED_APPS += APPS_DEPENDENCIES
INSTALLED_APPS += APPS_LIST_PACKAGES
INSTALLED_APPS += APPS_LIST


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'string_if_invalid': '-' if DEBUG else '',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

DATABASE_CONFIG = env.db_url('DATABASE_URL')
DATABASE_ROUTERS = ['conf.routers.SchemaRouter']
DATABASES = {
    'default': {
        **DATABASE_CONFIG,
        'OPTIONS': {'options': '-c search_path=module_schema,public'},
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = env('EMAIL_USE_TLS', cast=bool)
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
DEFAULT_SUPPORT_EMAIL = env('DEFAULT_SUPPORT_EMAIL')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'model_apps.authentication.permissions.IsUserAllowed',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'model_apps.core.jtw_authentication.JWTAuthentication',
    ],
    # 'EXCEPTION_HANDLER': 'model_apps.core.exceptions.custom_exception_handler',
    # 'DEFAULT_PAGINATION_CLASS': 'model_apps.core.mixins.pagination.PaginationMixin',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        # 'model_apps.core.filters.organization.OrganizationFilterBackend',
        # 'model_apps.core.filters.hierarchy.HierarchyFilterBackend',
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': '',
    'DESCRIPTION': Path(BASE_DIR / 'apps/docs/midia/overview.md').read_text(encoding='utf-8'),
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SECURITY': [
        {'bearerAuth': []},
    ],
    'COMPONENTS': {
        'securitySchemes': {
            'bearerAuth': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT',
            },
        },
    },
}
