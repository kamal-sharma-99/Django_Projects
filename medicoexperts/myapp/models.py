from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(max_length=35, unique=True)
    password=models.CharField(max_length=35)
    role=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_validate=models.BooleanField(default=False)

class Doctor(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    username=models.CharField(max_length=20,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    visiting_hours=models.CharField(max_length=20,null=True,blank=True)