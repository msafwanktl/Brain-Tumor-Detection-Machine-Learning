from django.db import models

# Create your models here.
class login(models.Model):
    username= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    usertype= models.CharField(max_length=10)

class user(models.Model):
    name= models.CharField(max_length=50)
    gender= models.CharField(max_length=10)
    dob= models.DateField()
    email= models.CharField(max_length=50)
    phone= models.BigIntegerField()
    housename= models.CharField(max_length=50)
    place= models.CharField(max_length=40)
    city= models.CharField(max_length=20)
    state= models.CharField(max_length=20)
    pincode=models.BigIntegerField()
    photo=models.CharField(max_length=400)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)

class doctor(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    DOB = models.DateField()
    email = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    housename = models.CharField(max_length=50)
    place = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.BigIntegerField()
    photo = models.CharField(max_length=400)
    Specialisation=models.CharField(max_length=100)
    HospitalName= models.CharField(max_length=100)
    About= models.CharField(max_length=400)
    Experience= models.CharField(max_length=100)
    Qualification= models.CharField(max_length=100)
    Status= models.CharField(max_length=100)
    LOGIN= models.ForeignKey(login,on_delete=models.CASCADE)

class schedule(models.Model):
    DOCTOR=models.ForeignKey(doctor,on_delete=models.CASCADE)
    date=models.DateField()
    start=models.CharField(max_length=10)
    end=models.CharField(max_length=10)

class appoinment(models.Model):
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    SCHEDULE=models.ForeignKey(schedule,on_delete=models.CASCADE)
    registrationDate=models.DateField()
    status=models.CharField(max_length=100)

class prescription(models.Model):
    APPOINMENT=models.ForeignKey(appoinment,on_delete=models.CASCADE)
    date=models.DateField()
    prescription=models.CharField(max_length=400)

class review(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    DOCTOR = models.ForeignKey(doctor, on_delete=models.CASCADE)
    date=models.DateField()
    review=models.CharField(max_length=400)