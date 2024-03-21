from django.shortcuts import render
from .models import News,Comment
from author.models import Publisher,Author
from django.http import JsonResponse
# Create your views here.
def view_news(request):
    db_news=News.objects.all()
    response=[]
    for news in  db_news:
        db_comment=Comment.objects.filter(article__pk=news.pk)
        com=[]
        for i in db_comment:
            com.append({
                "Comment":i.content,
                "By":{
                    "first_name":i.commented_by.first_name,
                    "last_name":i.commented_by.last_name
                }
            })
        response.append({
            "Title":news.title,
            "Desc":news.description,
            "date":news.date,
            
            "User":{
                "First_name":news.writer.first_name
            },
            "Comments":com
            
        })
    return JsonResponse(response,safe=False)