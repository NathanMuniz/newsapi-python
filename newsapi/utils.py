from __future__ import unicode_literals 

import datetime
import re
import sys 

__all__ = ("sringify_date_param",)

# Date in ISO-8601 format 
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_LEN = len("YYYY-MM-DD")
DATE_FMT = "%Y-%m-%d"

# Datetime in ISO-8601 format 
DATETIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$")
DATETIME_LEN = len("YYYY-MM-DDTHH:MM:SS")
DATETIME_FMT = ("%Y-%m-%dT%H:%M:%S")

def stringify_date_param(dt):
    if is_valid_string(dt):
        if len(dt) == DATE_LEN:
            validate_date_str(dt)
        elif len(dt) == DATETIME_LEN:
            validate_date_str(dt)
        else:
            raise ValueError("Date input sould be in format of either YYYYY-MM-DD ...")
        return dt 
    
    elif isinstance(dt, datetime.datetime):
        return dt.strftime(DATETIME_FMT)
    elif isinstance(dt, datetime.date):
        return dt.strftime(DATE_FMT)
    elif is_valid_num(dt):
        return datetime.datetime.utcfromtimestamp(dt).strftime(DATETIEM_FMT)
    else:
        raise TypeError("Date input must be onf of:")

def validate_date_str(datestr):
    if not DATE_RE.match(datestr):
        raise ValueError("Date input sould be in format of YYYY ...")

def validate_datetime_str(datetimestr):
    if not DATETIME_rE.MATCH(datimestr):
        raise ValueError("Datetime input shoud be in format of...")





