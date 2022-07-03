from django.db.models import (CharField, CASCADE, ImageField, ForeignKey, SET_NULL, FloatField)
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from apps.models.user import BaseModel


class Category(MPTTModel):
    emoji = CharField(max_length=255, null=True, blank=True)
    name = CharField(max_length=255, unique=True)
    description = CharField(max_length=1024)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)
    image = ImageField(upload_to='category/')


class Product(BaseModel):
    name = CharField(max_length=255, unique=True)
    category = ForeignKey('apps.Category', CASCADE)
    price = FloatField()
    image = ImageField(upload_to='product/')

