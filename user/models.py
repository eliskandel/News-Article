from django.db import models

# Create your models here.
class User(models.Model):
    user_name=models.CharField(max_length=200)
    first_name=models.CharField( max_length=50,null=False,blank=False)
    last_name=models.CharField(max_length=250,null=False,blank=False)
    age=models.IntegerField(default=18)
    def __str__(self) -> str:
        return self.first_name
