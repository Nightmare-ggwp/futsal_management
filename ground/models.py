from django.db import models

# Create your models here.
class Ground(models.Model):
   ground_id = models.AutoField(auto_created=True, primary_key=True)
   ground_name = models.CharField(max_length=30,default="")
   price = models.CharField(max_length=10,default="")
   player_capacity = models.CharField(max_length=10,default="")
   image = models.FileField(upload_to="ground/")

   class Meta:
       db_table = "ground"
