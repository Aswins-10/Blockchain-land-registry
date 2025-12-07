from django.db import models


# Create your models here.
from app.models import ureg
from works.models import NewWorks


class Complaint(models.Model):
    subject = models.CharField(max_length=124)
    complainttext = models.TextField(blank=False)
    username = models.ForeignKey(ureg, on_delete=models.SET_NULL, blank=True, null=True)
    projectname = models.ForeignKey(NewWorks, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.BooleanField(default=True)
    complaintdate = models.DateField(auto_now=True)
    upload = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.subject
