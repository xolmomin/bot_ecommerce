from django.core.validators import integer_validator
from django.db.models import (CharField, Model, ImageField, ForeignKey, CASCADE, EmailField, TextField, TimeField,
                              SET_NULL)


class Shop(Model):
    user = ForeignKey('apps.User', CASCADE)
    title = CharField(max_length=255)
    address = CharField(max_length=255, null=True, blank=True)
    bot_token = CharField(max_length=55, null=True, blank=True)
    about_us = TextField(null=True, blank=True)
    from_time = TimeField(default='09:00')
    to_time = TimeField(default='20:00')
    # geo_location = Jsonfield or geo


class Website(Model):
    shop = ForeignKey('apps.Shop', CASCADE)
    domain = CharField(max_length=155)
    image = ImageField(upload_to='website/slider/')


class CategorySub(Model):
    shop = ForeignKey('self', SET_NULL, null=True, blank=True)
    name = CharField(max_length=155)



class Slider(Model):
    website = ForeignKey(Website, CASCADE)
    # social_network = JsonField
    email = EmailField(null=True, blank=True)
    phone_number = CharField(max_length=25, validators=[integer_validator], null=True, blank=True)
    address = CharField(max_length=255, null=True, blank=True)
