from django.conf.urls.defaults import *
from piston.authentication import HttpBasicAuthentication
from piston.resource import Resource
from productAPI.product.handler import ProductHandler

auth = HttpBasicAuthentication(realm='My sample API')
products = Resource(handler=ProductHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^all/$', products),
    url(r'^(?P<id>[^/]+)/$', products),
    url(r'^$', products),
)


