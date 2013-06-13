from piston.emitters import Emitter
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.emitters import JSONEmitter, reverser, Emitter
from productAPI.product.models import Products, Attributes
import re

Emitter.register('json', JSONEmitter, 'application/json; charset=utf-8')

class ProductHandler(BaseHandler):
 
    fields = ('id',
              'vendor_style_number',
              'vendor_color',
              'vendor_size',
              ('attributes_set',('key','value')),
             )
    allowed_methods = ('GET', 'PUT', 'POST', 'DELETE')
    model = Products
    anonymous = 'AnonymousProductHandler'

    def read(self, request, id=None):
        action = request.REQUEST.get('action', None)
        
        if action == 'create':
            valid, attrs = Products.validate_request(request)
            if valid:
                p = Products.create(attrs)
                Attributes.create_or_update(p, attrs)
                return {'status':'success','product':p}
            else:
                return {'status':'error','message':'vendor_style_number, vendor_color, and vendor_size are required fields.'}
        elif action == 'update' and id:
            valid, attrs = Products.validate_request(request, id)
            p = Products.update(id, attrs)
            if p:
                Attributes.create_or_update(p, attrs)
                return {'status':'success','product':p}
            else:
                return {'status':'error','message':'Product does not exist.'}
        elif action == 'delete' and id:
            p = Products.objects.get(pk=id)
            p.delete()
            return {'status':'success'}

        else:
            if id:
                p = Products.objects.get(pk=id)
            else:
                p = Products.objects.all()
            return {'status':'success','product':p}


class AnonymousProductHandler(ProductHandler, AnonymousBaseHandler):
    pass




