from django.core.management.base import BaseCommand, CommandError
import csv,datetime
from ticket.models import Ticket
from type.models import Type

class Command(BaseCommand):
    help = 'Ingets (Imports) the specified TSV ticket file.'

    def add_arguments(self, parser):
        parser.add_argument('ifile', nargs='+', type=str)

    def handle(self, *args, **options):
            file_name = options['ifile'][0]
            self.stdout.write(self.style.SUCCESS('Starting Ingest for file: "%s"' % file_name))
            with open(file_name, newline='\n') as csvfile:
                filereader = csv.reader(csvfile, delimiter='\t', quotechar='|')
                count = 0
                for row in filereader:
                    if (count > 0):
                       # ONLY ingest clean data!!! #
                       #print(len(row))
                       #print(row[2])
                       if (len(row) == 11):
                           # First, create or get the type:
                           itm_type = Type.objects.get_or_create(label=row[4])[0]
                           create = True
                           try:
                                opened = datetime.datetime.strptime(row[5], '%m/%d/%Y %H:%M:%S')
                                #responded = datetime.datetime.strptime(row[6], '%m/%d/%Y %H:%M:%S')
                           except Exception as e:
                               try:
                                   opened = datetime.datetime.strptime(row[5], '%m/%d/%Y %H:%M')
                               except Exception as e:
                                   #responded = datetime.datetime.strptime(row[6], '%m/%d/%Y %H:%M')
                                   self.stdout.write(self.style.WARNING('Row %s does not contain correct timestamps for open: skipping...'%row[0]))
                                   create = False
                           try:
                                #opened = datetime.datetime.strptime(row[5], '%m/%d/%Y %H:%M:%S')
                                responded = datetime.datetime.strptime(row[6], '%m/%d/%Y %H:%M:%S')
                           except Exception as e:
                               try:
                                   responded = datetime.datetime.strptime(row[5], '%m/%d/%Y %H:%M')
                               except Exception as e:
                                   #responded = datetime.datetime.strptime(row[6], '%m/%d/%Y %H:%M')
                                   self.stdout.write(self.style.WARNING('Row %s does not contain correct timestamps for responded: skipping...'%row[0]))
                                   create = False                               
                           if create is True:
                           # Then create the ticket:
                               tkt = Ticket.objects.create(type=itm_type,opened=opened,responded=responded,affirmer=row[2],contributors=row[7],notes=row[8],reference=row[1],fix=row[8])
                               itm_type.tickets += 1
                               itm_type.updated = datetime.datetime.now()
                               itm_type.save()
                           #tkt.save()                           
                    count += 1
            self.stdout.write(self.style.SUCCESS('Successfully Ingested File "%s":  records.' % file_name))
import csv


