from mongoengine import *
import datetime
from microservices.date_functions import get_formatted_date


class Action(Document):
    action_type = StringField(required=True)
    amount = FloatField()  # Handle max/min values
    description = StringField(max_length=120)

    # handle later with datetime.now
    date = DateField(default=get_formatted_date()[0])
    time = StringField(default=get_formatted_date()[1])

    meta = {
        'db_alias': 'core',
        'collection': 'actions'
    }
