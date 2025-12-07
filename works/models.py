from django.db import models


# Create your models here.
from app.models import ureg


class District(models.Model):
    districtname = models.CharField(max_length=50)

    def __str__(self):
        return self.districtname


class Property(models.Model):
    LocationDetails = models.CharField(max_length=200)
    District = models.ForeignKey(District, on_delete=models.CASCADE)
    Place = models.CharField(max_length=200)
    Surveyno = models.IntegerField()
    PriceValue = models.IntegerField()
    Owner = models.ForeignKey(ureg, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    Tosell = models.BooleanField(default=False)

    def __str__(self):
        return self.LocationDetails


class PurchaseInterest(models.Model):
    PropertyName = models.ForeignKey(Property, on_delete=models.CASCADE)
    Interestee = models.ForeignKey(ureg, on_delete=models.CASCADE)
    Priceoffered = models.IntegerField()
    status = models.CharField(max_length=20,default='Waiting')


class OwnerShip(models.Model):
    PropertyName = models.ForeignKey(Property, on_delete=models.CASCADE)
    Owner = models.ForeignKey(ureg, on_delete=models.CASCADE)
    assignmentdate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)


class NewWorks(models.Model):
    ProjectDetails = models.CharField(max_length=200)
    District = models.ForeignKey(District, on_delete=models.CASCADE)
    Place = models.CharField(max_length=200)
    FundDetails = models.CharField(max_length=200)

    def __str__(self):
        return self.ProjectDetails


class WorkExpenditure(models.Model):
    ProjectName = models.ForeignKey(NewWorks, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    exp = models.IntegerField()
    status = models.BooleanField(default=True)
