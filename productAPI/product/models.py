import urllib
import os
from django.db import models
from django.core.files import File


class Products(models.Model):
    # Products all must have vendor_style_number, vendor_color, and vendor_size

    vendor_style_number  = models.CharField(max_length=140)
    vendor_color = models.CharField(max_length=140)
    vendor_size = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create(cls, attrs):
        entity, _ = cls.objects.get_or_create(vendor_style_number=attrs['vendor_style_number'], vendor_color=attrs['vendor_color'], vendor_size=attrs['vendor_size'])
        return entity

    @classmethod
    def update(cls, pk, attrs):
        import sys
        sys.stdout = sys.stderr
        print 'test'
        entity = cls.objects.filter(pk=pk)
        if entity:
            entity = entity[0]
            if 'vendor_style_number' in attrs:
                entity.vendor_style_number=attrs['vendor_style_number']
            if 'vendor_color' in attrs:
                entity.vendor_color=attrs['vendor_color']
            if 'vendor_size' in attrs:
                entity.vendor_size=attrs['vendor_size']
            entity.save()
            return entity
        return None

    @classmethod
    def validate_request(cls, request, pk=None):
        vendor_style_number = request.REQUEST.get('vendor_style_number', None)
        vendor_color = request.REQUEST.get('vendor_color', None)
        vendor_size = request.REQUEST.get('vendor_size', None)
        if vendor_style_number and vendor_color and vendor_size or pk:
            attrs = {}
            for key in request.REQUEST:
                if key != 'action':
                    attrs[key] = request.REQUEST.get(key)
            return True, attrs
        else:
            return False, None


class Attributes(models.Model):
    product = models.ForeignKey(Products)
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=30)

    @classmethod
    def create_or_update(cls, product, attrs):
       for key in attrs:
            if key not in ['action', 'vendor_style_number', 'vendor_color', 'vendor_size']:
                attribute, _ = cls.objects.get_or_create(key=key, product=product)
                attribute.value = attrs[key]
                attribute.save()


    @classmethod
    def delete_attrs(cls, product, attrs):
       for key in attrs:
            if key not in ['action', 'vendor_style_number', 'vendor_color', 'vendor_size']:
                attribute = cls.objects.filter(key=key, product=product)
                if attribute:
                    attribute.delete()


# Create your models here.
