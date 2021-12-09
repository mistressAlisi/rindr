from django.core.management.base import BaseCommand, CommandError
import csv,datetime
from ticket.models import Ticket
from type.models import Type

class Command(BaseCommand):
    help = 'Ingets (Imports) the specified CSV ticket file.'

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
                       if (len(row) == 10):
                           # First, create or get the type:
                           itm_type = Type.objects.get_or_create(label=row[3])[0]
                           try:
                                opened = datetime.datetime.strptime(row[4], '%m/%d/%Y %H:%M:%S')
                                responded = datetime.datetime.strptime(row[5], '%m/%d/%Y %H:%M:%S')
                           except:
                               self.stdout.write(self.style.WARNING('Row %s does not contain correct timestamps for open and responded, skipping...'%row[0]))
                           else:
                               self.stdout.write(self.style.MIGRATE_LABEL('Row %s being ingested...'%row[0]))
                           # Then create the ticket:
                           tkt = Ticket.objects.create(type=itm_type,opened=opened,responded=responded,affirmer=row[2],contributors=row[6],notes=row[7],reference=row[1],fix=row[7])
                           itm_type.tickets += 1
                           itm_type.updated = datetime.datetime.now()
                           itm_type.save()
                           #tkt.save()                           
                    count += 1
            self.stdout.write(self.style.SUCCESS('Successfully Ingested File "%s":  records.' % file_name))
import csv


