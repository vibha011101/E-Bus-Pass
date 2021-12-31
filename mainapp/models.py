from django.db import models
from django.db.models import deletion
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class student(models.Model):
    usn=models.CharField(max_length=10,primary_key=True)
    sname=models.CharField(max_length=25)
    saddress=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    branch=models.CharField(max_length=10)
    sem=models.IntegerField()
    photo=models.ImageField(upload_to="student", default="")
    password=models.CharField(max_length=25)


    class Meta:
        ordering=("usn","sname")

    def __str__(self):
        return f"{self.usn},{self.sname},{self.saddress},{self.email},{self.branch},{self.sem},{self.photo},{self.password} "

class place(models.Model):
    placeid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=25)

    class Meta:
        ordering=("placeid","pname")

    def __str__(self) :
        return f"{self.placeid},{self.pname} "

class bus(models.Model):
    busno=models.CharField(max_length=10)
    placeid=models.ForeignKey(place,on_delete=CASCADE)
    fees=models.IntegerField()
    class Meta:
        unique_together=(('busno','placeid'))
        ordering=("busno","placeid")

    def __str__(self):
        return f"{self.busno} "   

class payment(models.Model):
    reciptno=models.CharField(max_length=10,primary_key=True)
    date_of_pay=models.DateField()
    busno=models.ForeignKey(bus,on_delete=CASCADE)
    usn=models.ForeignKey(student,on_delete=CASCADE)
    validity=models.DateField()

    class Meta:
        ordering=("reciptno","date_of_pay")

    def __str__(self):
        return f"{self.reciptno}"

class goes_to(models.Model):
    busno=models.ForeignKey(bus,on_delete=CASCADE)
    placeid=models.ForeignKey(place,on_delete=CASCADE)
    boarding_time=models.TimeField()
    class Meta:
        unique_together=(('busno','placeid'))
        ordering=("busno","placeid")

    # def __str__(self):
        # return f"{self.busno}"    



