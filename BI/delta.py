import sys
import datetime
import holidays

class TimeCalc():
    BD_START = 10
    BD_STOP = 17
    
    def get_beginning_of_day(self,event):
        return datetime.datetime.fromisoformat(f"{self.get_day_string(event)} {self.BD_START}")

    def get_end_of_day(self,event):
        return datetime.datetime.fromisoformat(f"{self.get_day_string(event)} {self.BD_STOP}")

    def get_day(self,event):
        return datetime.datetime.fromisoformat(self.get_day_string(event))

    def get_day_string(self,event):
        return f"{event.year}-{event.month}-{event.day}"

    def get_next_day(self,event):
        return self.get_day(event) + datetime.timedelta(days=1)

    def is_work_day(self,event):
        if event.date() in holidays.US():
            return False
        if event.weekday() >= 5:
            return False
        return True


    def business_lapse(self,request, response):
        """ Note there is NO allowance for weekends or holidays.  Those can appear
            as a later upgrade.
        """
        if request > response:
            raise RuntimeError(f"How can there have been a response at {response} to a *later* request at {request}?")
        if request != response:
            beginning_of_request_day = self.get_beginning_of_day(request)
            if request < beginning_of_request_day:
                return self.business_lapse(min(beginning_of_request_day, response), response)
            end_of_response_day = self.get_end_of_day(response)
            if end_of_response_day < response:
                return self.business_lapse(request, max(end_of_response_day, request))
            request_day = self.get_day(request)
            new_request = self.get_next_day(request)
            if not self.is_work_day(request_day):
                return self.business_lapse(new_request, max(response, new_request))
            if not self.is_work_day(request_day) or request_day != self.get_day(response):
                assert request_day < self.get_day(response)
                return (max(request, self.get_end_of_day(request)) - request) + \
                        self.business_lapse(new_request, max(response, new_request))
            assert beginning_of_request_day <= request <= response <= end_of_response_day
        return response - request
