from django.db import models
from customer.models import Customer
# Create your models here.
class Cafe(models.Model):
   cafe_id = models.AutoField(auto_created=True, primary_key=True)
   item_name = models.CharField(max_length=30)
   customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
   price = models.CharField(max_length=10)
   description = models.CharField(max_length=100,default='')
   image = models.FileField(upload_to="images/cafe/")

   class Meta:
       db_table = "cafe"
