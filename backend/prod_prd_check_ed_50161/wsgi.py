"""
WSGI config for prod_prd_check_ed_50161 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "prod_prd_check_ed_50161.settings"
)

application = get_wsgi_application()
