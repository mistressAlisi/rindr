#!/usr/bin/python3
"""
Run "mypy --disallow-untyped-defs --ignore-missing-imports \
          --show-error-codes --strict-equality delta.py".

The holidays module lacks type hints.

Next need:  explicit Pytests.

Notice the imports are punctuated in an isort style.
"""
from datetime import datetime, timedelta,timezone
import sys
import holidays
us_holidays = holidays.UnitedStates()

class TimeCalc():
    BD_START = 10
    BD_STOP = 17
    # integer here: 0 is monday, 6 is sunday:
    WORKING_DAYS = 4
    # TIMEZONE:
    tzd = timedelta(hours=-8)
    tzo = timezone(tzd,name="PST")
    def business_lapse(self,opened,closed):
        # If we're in a holiday or not a work day - no lapse:
        if (opened.date() in us_holidays):
                print("Is Holday")
                return False
        if (opened.weekday() > self.WORKING_DAYS):
                print("Beyond WD")
                return False
        open_as_tz = opened.astimezone(self.tzo)
        if (open_as_tz.hour <= self.BD_START):
            # We are inside business hours:
            close_as_tz = closed.astimezone(self.tzo)
            print(close_as_tz.hour)
            if (close_as_tz.hour <= self.BD_STOP):
                # We're not going past closing hours:
                print("Normal Close")
                return close_as_tz - open_as_tz
            else:
                # Ticket is closed after BD stop so we'll take the lapse and start counting from the first minute of the next BD open:
                timedelta = close_as_tz - open_as_tz
                # Second set of deltas for calculation: the delta between the last BD close and the next one opening:
                BD_START_obj = datetime.strptime(f"{open_as_tz.year}/{open_as_tz.month}/{open_as_tz.day} {self.BD_STOP}:00:00","%Y/%m/%d %H:%M:%S")
                BD_STOP_obj = datetime.strptime(f"{close_as_tz.year}/{close_as_tz.month}/{close_as_tz.day} {self.BD_START}:00:00","%Y/%m/%d %H:%M:%S")
                # Subtract and return:
                return timedelta - (BD_STOP_obj-BD_START_obj)
        else:
            print("Before BD Start")
            return False
                
        
            
