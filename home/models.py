from django.db import models
from django.db.models import query
from django.db.models.fields.files import ImageField

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField()
    query=models.TextField()

class AddProduct(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(blank=True,null=True)
    description=models.TextField()
    image=models.ImageField(upload_to="home/index", default="",blank=True,null=True)
