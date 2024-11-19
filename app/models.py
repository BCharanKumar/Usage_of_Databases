from django.db import models

# Create your models here.
class School(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    add=models.TextField()

    def __str__(self):
        return self.sname
    
