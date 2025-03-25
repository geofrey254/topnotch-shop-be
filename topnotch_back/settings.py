"""
Django settings for topnotch_back project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import environ
from datetime import timedelta

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')


# PAYSTACK
PAYSTACK_SECRET_KEY = env('PAYSTACK_SECRET_KEY')
PAYSTACK_PUBLIC_KEY = env('PAYSTACK_PUBLIC_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['api.topnotchprintingpress.com/',
                 'www.api.topnotchprintingpress.com', 'localhost', 'http://*.127.0.0.1', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # django apps
    'products',
    'orders',
    'cart',
    'payments',

    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'corsheaders',
    'storages',
    'django_filters',
    'rest_framework_simplejwt',
    'django_extensions',


]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'topnotch_back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'topnotch_back.wsgi.application'

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.IsAuthenticated",
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 6,
    'MAX_PAGE_SIZE': 100,
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'access_type': 'online'
        },
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID'),
            'secret': env('GOOGLE_CLIENT_SECRET'),
            'key': ''
        }
    }
}

# storage settings
# AWS S3 Settings
# Storage settings for Django >= 4.2
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": env("AWS_STORAGE_BUCKET_NAME"),
            "endpoint_url": env("AWS_S3_ENDPOINT_URL"),
            "access_key": env("AWS_ACCESS_KEY_ID"),
            "secret_key": env("AWS_SECRET_ACCESS_KEY"),
            "region_name": env("AWS_S3_REGION_NAME"),
            "default_acl": "public-read",
            "querystring_auth": False,
            "file_overwrite": False,
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "bucket_name": env("AWS_STORAGE_BUCKET_NAME"),
            "endpoint_url": env("AWS_S3_ENDPOINT_URL"),
            "access_key": env("AWS_ACCESS_KEY_ID"),
            "secret_key": env("AWS_SECRET_ACCESS_KEY"),
            "region_name": env("AWS_S3_REGION_NAME"),
            "default_acl": "public-read",
            "querystring_auth": False,
            "location": "static",
        },
    },
}

# Base URL for static and media files
STATIC_URL = f'https://{env("AWS_STORAGE_BUCKET_NAME")}.{env("AWS_S3_ENDPOINT_URL").split("//")[1]}/static/'
MEDIA_URL = f'https://{env("AWS_STORAGE_BUCKET_NAME")}.{env("AWS_S3_ENDPOINT_URL").split("//")[1]}/media/'

# Local directories (optional, for development)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Redirect URLs
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SITE_ID = 4

# EMAIL SETUP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.brevo.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('BREVO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('BREVO_MASTER_PASSWORD')
DEFAULT_FROM_EMAIL = env('BREVO_FROM_EMAIL')

# Base URL for the frontend
FRONTEND_URL = 'http://localhost:3000'

# dj-rest-auth settings
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'jwt-refresh-token',
    "JWT_AUTH_HTTPONLY": False,
    'PASSWORD_RESET_USE_SITES_DOMAIN': True,
    'PASSWORD_RESET_CONFIRM_URL': 'http://localhost:3000/reset/confirm/{uid}/{token}/',
}


# SimpleJWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}


# CORS settings (allow your Next.js frontend)
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',
#     'http://127.0.0.1:3000',
#     'http://192.168.100:3000',
#     'http://127.0.0.1:8000'
# ]
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    'credentials',
    'X-CSRFToken',
    'Access-Control-Allow-Origin',
    'x-user-email',

    # Add other custom headers as needed
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
]
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_TRUSTED_ORIGINS = ['http://*.127.0.0.1', "http://localhost:3000",
                        'http://127.0.0.1:3000', 'http://192.168.100:3000', 'http://topnotchprintingpress.com']
# Allauth settings
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# SECRET_KEY="django-insecure-7a9xp0f9@-#0*2$w56k!ojstvlc2*b#470%2y_=o1pq#actmj="
