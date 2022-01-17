from django.db import models
from django.contrib import admin
# Create your models here.


class Cause(models.Model):
    cause_id = models.TextField(max_length=200,verbose_name='Cause ID')
    label = models.TextField(max_length=200,verbose_name='Cause Label')
    created = models.DateTimeField(auto_now_add=True,editable=False,verbose_name='Cause Created')
    updated = models.DateTimeField(auto_now=True,editable=False,verbose_name='Cause Updated')
    tickets = models.IntegerField(verbose_name='Ticket Count',null=True,blank=True,default=0)
    def __str__(self):
        return "Ticket Cause: "+self.label

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    pass
