from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^products/', include('productAPI.product.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
