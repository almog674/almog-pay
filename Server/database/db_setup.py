import mongoengine


def initialize_db():
    mongoengine.connect(alias='core', name='almog_pay',
                        host='localhost:27017')
