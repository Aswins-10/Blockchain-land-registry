from django.db import models


# Create your models here.
# class login(models.Model):
#     username=models.CharField(max_length=200)
#     password=models.CharField(max_length=200)
#     confirm_password=models.CharField(max_length=200)

# class clogin(models.Model):
#     username=models.CharField(max_length=200)
#     password=models.CharField(max_length=200)

class ureg(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200, unique=True)
    password=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    mp=models.CharField(max_length=200)
    ward=models.CharField(max_length=200)


class creg(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    # mp=models.CharField(max_length=200)
    ward=models.CharField(max_length=200)


class ngoreg(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    mob=models.CharField(max_length=200)
    # mp=models.CharField(max_length=200)
    ward=models.CharField(max_length=200)

class upload(models.Model):
    complaint=models.CharField(max_length=200)
    newidea=models.CharField(max_length=200)


class newproject(models.Model):
    projectdetails=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    funddetails=models.CharField(max_length=200)


class expenditure(models.Model):    
     projectname=models.CharField(max_length=200)
     description=models.CharField(max_length=200)
     exp=models.CharField(max_length=200)
     status = models.BooleanField(default=False)