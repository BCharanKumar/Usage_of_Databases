from django.db import models

# Create your models here.
class Country(models.Model):
    cname=models.CharField(max_length=125)
    cid=models.IntegerField(primary_key=True)
    def __str__(self):
        return self.cname
    
class Capital(models.Model):
    cid=models.OneToOneField(Country,on_delete=models.CASCADE)
    capital_id=models.IntegerField(primary_key=True)
    capital_name=models.CharField(max_length=75)

    def __str__(self):
        return self.capital_name