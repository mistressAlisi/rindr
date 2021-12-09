from django.db import models
from django.contrib import admin
from type.models import Type
from django.contrib.auth.models import User
# Create your models here.


class Ticket(models.Model):
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
    lapse  = models.DurationField(verbose_name="Business Lapse",blank=True,null=True)
    delta  = models.DurationField(verbose_name="Business Lapse Delta",blank=True,null=True)
    def __str__(self):
        return "Ticket: {} ".format(str(self.id))
    
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

class TicketMeanTimes(models.Model):
        mean_response = models.DurationField(verbose_name="Mean Time to Response")
        ticket_count = models.IntegerField(verbose_name='Ticket Count')
        class Meta:
            managed = False
            db_table = 'ticket_meantimes'
