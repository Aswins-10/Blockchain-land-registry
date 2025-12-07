from django.db import models

# Create your models here.
from app.models import ureg
from works.models import NewWorks, Property


class Donate(models.Model):
    projectname = models.ForeignKey(NewWorks, on_delete=models.SET_NULL, blank=True, null=True)
    remarks = models.CharField(max_length=124)
    amount = models.FloatField()
    username = models.ForeignKey(ureg, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.BooleanField(default=True)
    depositdate = models.DateField(auto_now=True)
    prevhash= models.CharField(max_length=224, blank=True, null=True)
    hash = models.CharField(max_length=224, blank=True, null=True)
    def __str__(self):
        return self.projectname


class Block(models.Model):
    projectname = models.ForeignKey(Property, on_delete=models.SET_NULL, blank=True, null=True)
    username = models.ForeignKey(ureg, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.BooleanField(default=True)
    depositdate = models.DateField(auto_now=True)
    prevhash= models.CharField(max_length=224, blank=True, null=True)
    hash = models.CharField(max_length=224, blank=True, null=True)

    def __str__(self):
        return self.projectname


