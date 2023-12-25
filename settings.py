import os
import environ


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = environ.Env()
environ.Env.read_env()

# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = env('DJANGO_SECRET_KEY')

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

DATABASES = {
    "default": env.db("DATABASE_URL")
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

INSTALLED_APPS = ("db",)

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
