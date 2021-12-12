from django.db import models
from django.contrib import admin
from type.models import Type
from django.contrib.auth.models import User
# Create your models here.


class Ticket(models.Model):
    SystemTable = (('o'),('ODINs')),(('b'),('BlueJays')),(('m'),('Mattermost')),(('k'),('BuildKite'))
    DifficultyTable = (('1'),('1  - Simplest (Did you RTFM?)')),(('2'),('2')),(('3'),('3')),(('4'),('4')),(('5'),('5')),(('6'),('6 - Bloody hard. (My name is Neo.)'))
    ticket_id = models.TextField(max_length=200,verbose_name='Ticket ID')
    type = models.ForeignKey(Type,verbose_name = 'Ticket Type',on_delete=models.RESTRICT)
    creator = models.ForeignKey(User,verbose_name = "User",on_delete=models.RESTRICT,null=True)
    created = models.DateTimeField(auto_now_add=True,editable=False,verbose_name='Ticket Created')
    updated = models.DateTimeField(verbose_name='Ticket Updated',auto_now_add=True)
    opened = models.DateTimeField(verbose_name='Ticket Initially Opened')
    responded = models.DateTimeField(verbose_name='Ticket Initial Response')
    affirmer = models.TextField(max_length=200,verbose_name='Ticket for Affirmer')
    notes = models.TextField(verbose_name='Ticket Notes',null=True)
    reference = models.TextField(verbose_name='Ticket Reference',null=True)
    contributors = models.TextField(verbose_name='Ticket Contributors',null=True)
    fix = models.TextField(verbose_name='Ticket Fix',null=True)
    archived = models.BooleanField(verbose_name="Ticket Archived",default=False)
    team = models.TextField(max_length=200,verbose_name='Ticket for DT/Team',default="N/A")
    system = models.CharField(choices=SystemTable,max_length=2,verbose_name="Ticket originated in System",default='o')
    difficulty = models.CharField(choices=DifficultyTable,max_length=2,verbose_name="Ticket Debug Difficulty",default='2')
    regression = models.BooleanField(default=False,verbose_name="Regression related")
    regression_url = models.TextField(verbose_name="Regression / Build URL",null=True)
    exported = models.BooleanField(default=False,verbose_name="Record Exported")
    def __str__(self):
        return "Ticket: #{} for Affirmer: {} of team: {} ".format(str(self.id),self.affirmer,self.team)
    
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

class TicketMeanTimes(models.Model):
        mean_response = models.DurationField(verbose_name="Mean Time to Response")
        ticket_count = models.IntegerField(verbose_name='Ticket Count')
        class Meta:
            managed = False
            db_table = 'ticket_meantimes'

class TicketWeeklyResponseTimes(models.Model):
        mode = models.DurationField(verbose_name="Mode Response Time")
        week = models.IntegerField(verbose_name='Calendar Week')
        year = models.IntegerField(verbose_name='Calendar Year')
        count = models.IntegerField(verbose_name='Ticket Count')
        class Meta:
            managed = False
            db_table = 'ticket_mode_response_per_week_view'

