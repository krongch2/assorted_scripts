import random
import time
import pytz
from django.utils.dateparse import parse_datetime

def convert_time(t, fmt):

    # format mktime to string time
    fmttime = time.strftime(fmt, time.localtime(t))

    # convert time string into an aware datetime
    # https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/
    return pytz.timezone('Asia/Bangkok').localize(parse_datetime(fmttime), is_dst=None)

def random_date(start, end, fmt):

    # get floting point number in seconds from start time
    stime = time.mktime(time.strptime(start, fmt))

    # do the same for end time
    etime = time.mktime(time.strptime(end, fmt))

    # get a random time (in seconds) between the two
    ptime = stime + random.random() * (etime - stime)
    return ptime

fmt = '%Y-%m-%d %H:%M:%S'
ptime = random_date('2012-02-01 00:00:00', '2017-05-05 00:00:00', fmt)
print(convert_time(ptime, fmt))
print(convert_time(ptime + random.randint(30, 600), fmt))
