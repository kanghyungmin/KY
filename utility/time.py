import string
import time
from datetime import datetime


def convertTimestamp2Str(p_time: float) -> string:
    return str(p_time)

def convertDatetime2Str(p_time: datetime) -> string:
    return p_time.strftime('%T-%m-%d %H:%M:%S')

def convertStr2Timestamp(p_time: string) -> float:
    return time.mktime(datetime.strptime(p_time, '%Y-%m-%d %H:%M:%S').timetuple())

def convertDatetime2Timestamp(p_time: datetime) -> float:
    return time.mktime(p_time.timetuple())

def convertStr2Datetime(p_time: string) -> datetime:
    return datetime.strptime(p_time, '%Y-%m-%d %H:%M:%S')

def convertTimestamp2Datetime(p_time: float) -> datetime:
    return datetime.fromtimestamp(p_time)
