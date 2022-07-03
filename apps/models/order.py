from django.db.models import (CharField, CASCADE, ForeignKey, BooleanField)

from apps.models.user import BaseModel


class Order(BaseModel):
    NEW = 'new'
    CONFIRMED = 'confirmed'
    CANCELED = 'canceled'
    STATUS = (
        (NEW, 'new'),
        (CONFIRMED, 'confirmed'),
        (CANCELED, 'canceled')
    )

    CASH = 'cash'
    TERMINAL = 'terminal'
    PAYMENT_TYPE = (
        (CASH, 'cash'),
        (TERMINAL, 'terminal')
    )
    customer = ForeignKey('apps.Customer', CASCADE)
    status = CharField(max_length=15, choices=STATUS, default=NEW)
    payment_status = BooleanField(default=False)
    payment_type = CharField(max_length=15, choices=PAYMENT_TYPE, default=CASH)
