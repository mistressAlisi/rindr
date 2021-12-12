#!/usr/bin/python3
"""
Run "mypy --disallow-untyped-defs --ignore-missing-imports \
          --show-error-codes --strict-equality delta.py".

The holidays module lacks type hints.

Next need:  explicit Pytests.

Notice the imports are punctuated in an isort style.
"""
from datetime import datetime, timedelta
import sys

import holidays


EVENT = datetime
fromisoformat = datetime.fromisoformat


class TimeCalc():
    BD_START = 10
    BD_STOP = 17
    
    def _get_beginning_of_day(self,event: EVENT) -> EVENT:
        return fromisoformat(f"{self._get_day_string(event)} {self.BD_START}:00")

    def _get_end_of_day(self,event: EVENT) -> EVENT:
        return fromisoformat(f"{self._get_day_string(event)} {self.BD_STOP}")

    def _get_day(self,event: EVENT) -> EVENT:
        return fromisoformat(self._get_day_string(event))

    def _get_day_string(self,event: EVENT) -> str:
        return f"{event.year}-{event.month}-{event.day}"

    def _get_next_day(self,event: EVENT) -> EVENT:
        return self._get_day(event) + timedelta(days=1)

    def _is_work_day(self,event: EVENT) -> bool:
        if event.date() in holidays.US():
            return False
        if event.weekday() >= 5:
            return False
        return True

    def business_lapse(self,request: EVENT, response: EVENT) -> timedelta:
        """ This is the entry point most clients will want to use.
        """
        if request > response:
            raise RuntimeError(f"How can there have been a response at {response} to a *later* request at {request}?")
        if request != response:
            beginning_of_request_day = self._get_beginning_of_day(request)
            if request < beginning_of_request_day:
                return self.business_lapse(min(beginning_of_request_day, response), response)
            end_of_response_day = self._get_end_of_day(response)
            if end_of_response_day < response:
                return self.business_lapse(request, max(end_of_response_day, request))
            request_day = self._get_day(request)
            new_request = self._get_next_day(request)
            if not self._is_work_day(request_day):
                return self.business_lapse(new_request, max(response, new_request))
            assert self._is_work_day(request_day)
            if request_day != self._get_day(response):
                assert request_day < self._get_day(response)
                return (max(request, self._get_end_of_day(request)) - request) + \
                        self.business_lapse(new_request, max(response, new_request))
            assert beginning_of_request_day <= request <= response <= end_of_response_day
        return response - request


def main() -> None:
    """ Examples:
            ./delta.py "2021-10-27 03:45" "2021-10-29 11:08"
            ./delta.py "2021-10-27 03:45" "2021-10-29 11:08"
            ./delta.py "2021-10-27 03:45" "2021-10-29 20:08"
            ./delta.py "2021-10-27 13:45" "2021-10-27 14:08"
            ./delta.py "2021-10-27 13:45" "2021-10-28 14:08"
            ./delta.py "2021-10-27 03:45" "2021-10-27 05:58"
            ./delta.py "2021-10-27 10:00" "2021-10-28 17:00"
            ./delta.py "2021-10-27 10:00" "2021-10-30 10:20"
            ./delta.py "2021-10-27 18:00" "2021-10-27 20:20"
            ./delta.py "2021-11-27 03:45" "2021-11-29 20:08"
            ./delta.py "2021-11-27 13:45" "2021-11-27 14:08"
            ./delta.py "2021-11-27 13:45" "2021-11-28 14:08"
            ./delta.py "2021-11-27 03:45" "2021-11-27 05:58"
            ./delta.py "2021-11-27 10:00" "2021-11-28 17:00"
            ./delta.py "2021-11-27 10:00" "2021-11-30 10:20"
            ./delta.py "2021-11-27 18:00" "2021-11-27 20:20"
    """
    request_time = fromisoformat(sys.argv[1])
    response_time = fromisoformat(sys.argv[2])
    print(f"Times are {request_time} and {response_time}.")
    print(f"Difference is {response_time - request_time}.")
    print(f"Business lapse is {TimeCalc().business_lapse(request_time, response_time)}.")


if __name__ == "__main__":
    main()
