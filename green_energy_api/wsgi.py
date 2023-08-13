import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "green_energy_api.settings.local")

application = get_wsgi_application()
