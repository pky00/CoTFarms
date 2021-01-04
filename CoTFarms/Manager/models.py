from django.db import models
from django.utils import timezone
from datetime import date

class CowType(models.Model):
    Type = models.CharField(max_length=30)

    def __str__(self):
        return self.Type

class Cow(models.Model):
    Gender = (("M","MALE"),("F","FEMALE"))
    
    number = models.IntegerField(primary_key=True)
    dob = models.DateField()
    Type = models.ForeignKey(CowType, on_delete=models.SET_NULL, null=True)
    mother = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True )
    gender = models.CharField(choices=Gender,max_length=1)
    dead = models.BooleanField(default=False)
    isMilking = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number) + " " + str(self.Type)

class CowMilking(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    date = models.DateTimeField(default=date.today)

class CowMilkSale(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    price = models.FloatField()

class CowPregnancy(models.Model):
    cow = models.ForeignKey(Cow,on_delete=models.CASCADE)
    dop = models.DateTimeField() #date of pregnancy