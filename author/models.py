from django.db import models

# Create your models here.
   
class Publisher(models.Model):
    name=models.CharField(max_length=240, null=False,blank=False)
    price=models.IntegerField(default=100, null=False, blank=False)
    # created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
class Author(models.Model):
    name=models.CharField(max_length=240, null=False,blank=False)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name
 