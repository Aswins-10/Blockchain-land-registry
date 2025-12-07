from django.db import models


# Create your models here.
from app.models import ureg
from works.models import NewWorks


class Comment(models.Model):
    commenttext = models.TextField(blank=False)
    username = models.ForeignKey(ureg, on_delete=models.SET_NULL, blank=True, null=True)
    projectname = models.ForeignKey(NewWorks, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.BooleanField(default=True)
    commentdate = models.DateField(auto_now=True)

    def __str__(self):
        return self.commenttext
