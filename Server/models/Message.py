from mongoengine import *
import datetime
from microservices.date_functions import get_formatted_date


class Message(Document):
    description = StringField(required=True, max_length=120)
    date = DateField(default=get_formatted_date()[0])
    time = StringField(default=get_formatted_date()[1])
    mark = BooleanField(default=False)

    meta = {
        'db_alias': 'core',
        'collection': 'messages'
    }
