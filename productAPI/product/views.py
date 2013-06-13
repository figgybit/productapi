from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from productAPI.product.models import Products
from django.core import serializers

def index(request):
    p = Products.objects.filter(pk=1)
    return HttpResponse(serializers.serialize("json", p), mimetype='application/json')
    # return HttpResponse(p.vendor_style_number)

