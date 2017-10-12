from django.shortcuts import render,render_to_response
from .models import article,article_pic,article_tag
# Create your views here.
#http://www.cnblogs.com/yangmv/p/5327477.html
def index(request):
    articles=article.objects.all().values('title','author','date','content')[:1]
    #return render_to_response('index.html',articles)
    return render(request,'index.html',{'articles':articles})