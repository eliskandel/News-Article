from django.db import models
from author.models import Author
from user.models import User
# Create your models here.
class News(models.Model):
    title=models.CharField(max_length=230, null=False, blank=False)
    description=models.CharField(max_length=1000,null=False)
    date=models.DateTimeField(auto_now_add=True)
    writer=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    content=models.CharField(max_length=250, null=False, blank=False)
    article=models.ForeignKey(News, on_delete=models.CASCADE,null=True,blank=True)
    commented_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.commented_by.user_name