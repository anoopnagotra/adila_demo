"""
WSGI config for riwaz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys


sys.path.append("/var/www/python/riwaz/myenv")

sys.path.append("/var/www/python/riwaz/myenv/lib")

sys.path.append("/var/www/python/riwaz/myenv/lib/python3.6")

sys.path.append("/var/www/python/riwaz/myenv/lib/python3.6/site-packages")
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'riwaz.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from whitenoise import WhiteNoise


application = WhiteNoise(application, root='staticfiles')
application.add_files('staticfiles', prefix='static/')
