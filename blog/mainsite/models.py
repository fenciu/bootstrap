from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.



class article_pic(models.Model):
    article_id=models.IntegerField(default=None)
    url=models.FileField(upload_to='./upload/')
    #def __str__(self):
    #    return self.url+"123"

class article_tag(models.Model):
    article_id=models.IntegerField(default=None)
    tag_name=models.CharField(max_length=30)
    def __str__(self):
        return self.tag_name

class article(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    date=models.DateTimeField(default=timezone.now)
    content=RichTextField(default=None)
    article_pic=models.ForeignKey(article_pic,on_delete=models.CASCADE)
    article_tag=models.ForeignKey(article_tag,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['date']
