from mongoengine import *
from .Action import Action


class Transaction(Action):
    user_sender = StringField(required=True)
    user_reciever = StringField(required=True)
    confirm = BooleanField(default=False)

    meta = {
        'db_alias': 'core',
        'collection': 'transactions'
    }
