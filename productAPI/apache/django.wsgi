import os, sys
sys.path.append('/www')
os.environ['DJANGO_SETTINGS_MODULE'] = 'productAPI.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
