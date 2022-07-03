from django.contrib.auth.models import AbstractUser
from django.core.validators import integer_validator
from django.db.models import (CharField, EmailField, ForeignKey, CASCADE)

from apps.models.custom_base import BaseModel, UserManager


class User(AbstractUser):
    email = EmailField(unique=True)
    phone_number = CharField(max_length=25, unique=True, validators=[integer_validator])
    address = CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Customer(BaseModel):
    shop = ForeignKey('apps.Shop', CASCADE)
    first_name = CharField(max_length=70, null=True, blank=True)
    last_name = CharField(max_length=70, null=True, blank=True)
    username = CharField(max_length=70, null=True, blank=True)
    phone_number = CharField(max_length=25, validators=[integer_validator], null=True, blank=True)
