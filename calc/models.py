from django.db import models


class datas(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood = models.CharField(max_length=100)
    phone = models.IntegerField()

class user:
    username: str   

class users:
    username : str

class reg(models.Model):
    username = models.CharField(max_length=100)    
    email = models.EmailField(max_length=100)
    password= models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    