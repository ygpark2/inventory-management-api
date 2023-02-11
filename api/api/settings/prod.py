import os
import dj_database_url

from .base import *


SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

ALLOWED_HOSTS = [".herokuapp.com"]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Enable WhiteNoise's GZip compression of static assets.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

if "DATABASE_URL" in os.environ:
    MAX_CONN_AGE = 600

    # Configure Django for DATABASE_URL environment variable.
    db_url_from_env = dj_database_url.config(conn_max_age=MAX_CONN_AGE, ssl_require=True)
    DATABASES['default'].update(db_url_from_env)

    # Enable test database if found in CI environment.
    if "CI" in os.environ:
        DATABASES["default"]["TEST"] = DATABASES["default"]


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
