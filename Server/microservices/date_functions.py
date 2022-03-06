import datetime


def get_formatted_date():
    date = datetime.datetime.now()
    only_date = str(date).split('.')[0]
    date, time = only_date.split(' ')
    return date, time
