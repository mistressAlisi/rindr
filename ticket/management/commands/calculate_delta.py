from django.core.management.base import BaseCommand, CommandError
import csv,datetime
from ticket.models import Ticket
from type.models import Type
from BI.delta import TimeCalc
class Command(BaseCommand):
    help = 'Calculates BI times and deltas for all tickets'
    timeObj = TimeCalc()


    def handle(self, *args, **options):
            tickets = Ticket.objects.filter(archived=False)
            count = 0;
            for t in tickets:
                #print(t.opened.strftime('%Y-%m-%d %H:%M'))
                #print(t.responded)
                print(self.timeObj.business_lapse(t.opened.strftime('%Y-%m-%d %H:%M'),t.responded.strftime('%Y-%m-%d %H:%M')))
                count +=1
            self.stdout.write(self.style.SUCCESS(f'Successfully Processed {count} records.'))



