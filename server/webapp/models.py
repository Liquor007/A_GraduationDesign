from django.db import models

# Create your models here.
class Users(models.Model):
    uid=models.AutoField(primary_key=True)
    email=models.CharField(max_length=320, unique=True)
    password=models.CharField(max_length=20)
    class Meta:
        db_table='users'