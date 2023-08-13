from .base import *  # noqa
from .base import env


SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="RWQbBfOERt6JaOQsyek49VkoeyWBpvoHuo9q7hKrDqMbRsettCk",
)

DEBUG = True


CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

DEFAULT_FROM_EMAIL = "vicente19981@live.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Green Energy"
