"""
Django settings for store project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1a!e^^yplyud2)4pw$c+@*zs!ddry=!3gw-2xt+eq1htn%2uq)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']
DOMAIN_NAME = 'http://127.0.0.1:8000'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'products',
    'user',
    'orders',
    'debug_toolbar',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    'allauth.account.middleware.AccountMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

ROOT_URLCONF = 'store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'products.context_processor.basket',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'store.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "store_db",
        "USER": "store_user",
        "PASSWORD": "dimasereda22D",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# User
AUTH_USER_MODEL = 'user.User'
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Sending email
EMAIL_HOST = 'smtp.yandex.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'll-O-E-Xa-l-i@yandex.by'
EMAIL_HOST_PASSWORD = 'awdszxca200122D'
# EMAIL_USE_SSL = True
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# OAuth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}

# Strike Payment
STRIPE_PUBLIC_KEY = 'pk_test_51OLWBJCO7SrDNfqXYwOc0GYWvkZoFsRTAWTNFbbZgHwyQ20pVC4ZHO4QYH1myk3PeOpVlmj5Yxf9N010bRamj3Os000TufifdV'
STRIPE_SECRET_KEY = 'sk_test_51OLWBJCO7SrDNfqX75GIruwqiHNNBJod3cOwVQ54AbNdm0urRF32dkrSkW3WQ1BkG5BDeNdtuIzgF8oinyqxIVwz00kfxgGh11'
SRTIPE_WEBHOOK_SECRET = 'whsec_d5e340ac9e0650bcb63d079611dde82cbd04722f1dc454e6384d5f5de460f9df'