from django.conf import settings
import pytz
from django.utils import timezone
zh = pytz.timezone(settings.TIME_ZONE)

def tz_parser_nozone(time):
  if time:
    time_wzone = timezone.datetime(year=int(time[0:4]), month=int(time[5:7]), day=int(time[8:10]), tzinfo=timezone.get_current_timezone())
    return time_wzone
  else:
    return None