from email.policy import default
import mongoengine


class User(mongoengine.Document):
    username = mongoengine.StringField(
        max_length=20, min_length=5, required=True, unique=True)
    email = mongoengine.EmailField(required=True, unique=True)
    password = mongoengine.StringField(required=True)
    account_id = mongoengine.IntField()  # handle later

    account_balance = mongoengine.FloatField(default=0)
    all_time_high = mongoengine.FloatField(default=0)
    all_time_low = mongoengine.FloatField(default=0)

    # Handle history
    inbox = mongoengine.ListField()
    frame = mongoengine.IntField(default=0)

    rule = mongoengine.StringField(default='User')
    actions = mongoengine.ListField(default=[])

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
