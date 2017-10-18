from django.shortcuts import render,render_to_response
from .models import article,article_pic,article_tag
from django.http import HttpResponse,request
# Create your views here.
#http://www.cnblogs.com/yangmv/p/5327477.html

def index(request):
    articles=article.objects.all()
    #return render_to_response('index.html',articles)
    #print (articles[0]['title'])
    return render(request,'index.html',{'articles':articles})
def article_de(request,param1):
    
    
    articles_dea=article.objects.get(id=param1)
    return render(request,'article.html',{'articles_dea':articles_dea})
def article_search(request,param1):
    print(param1)
    articles_sea_dea=article.objects.filter(title__contains=param1)
    if articles_sea_dea:

        pass
    else:
        articles_sea_dea=""
    return render(request,"search.html",{'articles_sea_dea':articles_sea_dea})

def article_aside(request):
    ar="123"
    return render(request,"aside.html",{'ar':ar})