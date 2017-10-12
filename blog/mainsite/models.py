from django.db import models

# Create your models here.
class article(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    date=models.DateField()
    content=models.CharField
    


class article_pic(models.Model):
    article_id=models.IntegerField()
    url=models.FileField(upload_to='./upload/')

class article_tag(models.Model):
    article_id=models.IntegerField()
    tag_name=models.CharField(max_length=30)

