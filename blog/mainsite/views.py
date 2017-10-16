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
def article_de(request):
    article_id=request.GET.get('id')
    print(article_id)
    return render(request,'article.html')