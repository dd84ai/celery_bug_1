"""
Django settings for testdjangoapp project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
import secrets
from pathlib import Path
from typing import Any, Dict, List

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.token_hex(32)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS: List[str] = []

# Application definition

INSTALLED_APPS = [
    "testdjangoapp.exampleapp",
    "package.packagedjintegration",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "testdjangoapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "testdjangoapp.wsgi.application"

APP_DATABASE_USER = os.environ.get("APP_DATABASE_USER", "postgres")
APP_DATABASE_PASSWORD = os.environ.get("APP_DATABASE_PASSWORD", "postgres")
APP_DATABASE_HOST = os.environ.get("APP_DATABASE_HOST", "localhost")
APP_MAIN_DB = os.environ.get("APP_MAIN_DB", "default")

additional_dbs = os.environ.get("APP_ADDITIONAL_DATABASES", "postgres")
APP_ADDITIONAL_DATABASES = additional_dbs.split(",") if additional_dbs != "" else []
APP_DATABASE_PORT = os.environ.get("APP_DATABASE_PORT", "5432")

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {}


def generate_db_settings(db_name: str) -> Dict[str, Any]:
    return {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": db_name,
        "USER": APP_DATABASE_USER,
        "PASSWORD": APP_DATABASE_PASSWORD,
        "HOST": APP_DATABASE_HOST,
        "PORT": APP_DATABASE_PORT,
    }


DATABASES["default"] = generate_db_settings(APP_MAIN_DB)

for DATABASE_NAME in APP_ADDITIONAL_DATABASES:
    DATABASES[DATABASE_NAME] = generate_db_settings(DATABASE_NAME)


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

config = os.environ

CELERY_BROKER_URL = config.get("STATUS_STORAGE", "redis://localhost:6379")
CELERY_RESULT_BACKEND = config.get("RESULT_STORAGE", "redis://localhost:6379")
# Copy pasted from Butter App
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "visibility_timeout": 3600 * 24,  # 24 hour
    "fanout_prefix": True,
    "fanout_patterns": True,
}
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]  # Ignore other content
CELERY_RESULT_SERIALIZER = "json"
CELERY_WORKER_LOG_FORMAT = "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"
CELERY_WORKER_TASK_LOG_FORMAT = "[%(asctime)s: %(levelname)s/%(processName)s][%(task_name)s(%(task_id)s)] %(message)s"  # NOQA
CELERYD_LOG_FORMAT = "[%(asctime)s] %(levelname)s/%(hostname)s/%(processName)s tid=%(task_id)s %(module)s %(message)s"  # NOQA

CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
