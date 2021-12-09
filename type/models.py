from django.db import models
from django.contrib import admin
# Create your models here.


class Type(models.Model):
    type_id = models.TextField(max_length=200,verbose_name='Type ID')
    label = models.TextField(max_length=200,verbose_name='Type Label')
    created = models.DateTimeField(auto_now_add=True,editable=False,verbose_name='Type Created')
    updated = models.DateTimeField(auto_now=True,editable=False,verbose_name='Type Updated')
    tickets = models.IntegerField(verbose_name='Ticket Count',null=True,blank=True,default=0)
    def __str__(self):
        return "Ticket Type: "+self.label
    
@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass
