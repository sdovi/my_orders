"""
Django settings for gtrfx project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv('.env')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--q8gn50572qkpkee58-7w@96i-rzlu34*b5=o+plq8r_8z0dqu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]

CSRF_TRUSTED_ORIGINS = ['https://gtrobot.shop', 'http://gtrobot.shop', 'https://viper-pro-turtle.ngrok-free.app']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5502',
    'https://gtrobot.shop',
    'https://www.gtrobot.shop',
    'http://gtrobot.shop',
    'http://www.gtrobot.shop',
]
CORS_ALLOW_CREDENTIALS = True
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'accounts.apps.AccountsConfig',

    'pyclick',
    'rest_framework',
    'rest_framework.authtoken',
    'payments.apps.PaymentsConfig',
    
]

CLICK_SETTINGS = {
    'service_id': os.getenv('CLICK_SERVICE_ID'),
    'merchant_id': os.getenv('CLICK_MERCHANT_ID'),
    'secret_key': os.getenv('CLICK_SECRET_KEY'),
    'merchant_user_id': os.getenv('CLICK_MERCHANT_USER_ID'),
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gtrfx.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'gtrfx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = Path(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = Path(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'


TWILIO_ACCOUNT_SID = 'ACa09257eb5d916af2ebd5614a4d0caac4'
TWILIO_AUTH_TOKEN = '5fde81986b18212b45ecdeb2543c28e5'
TWILIO_SERVICE_ID = "VA982840e9c71108cc56dbf5dba27b200e"
TWILIO_WHATSAPP_NUMBER = "+13158193649"

ESKIZ_USERNAME = "mirmakhamat@gmail.com"
ESKIZ_PASSWORD = "AVvpDtUwq06XofiQjvBIhYuLQogOLK1FIqgzRjIp"


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'filename': 'logs.log',
#         },
#     },
#     'root': {
#         'handlers': ['console', 'file'],
#         'level': 'INFO',
#     },
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

SERVER_URL = "https://gtrobot.shop/"

YOOKASSA_ACCOUNT_ID = '354261'
YOOKASSA_SECRET_KEY = 'live_qpgGElO5RL-2TQAQLG-vJQ6yikgU-NriCaL5oW1113Q'
YOOKASSA_WEBHOOK_URL = 'https://api.gtrobot.shop/payments/yookassa/webhook/'