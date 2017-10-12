from django.db import models

# Create your models here.
class article(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    date=models.DateTimeField()
    content=models.TextField(default=None)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['date']


class article_pic(models.Model):
    article_id=models.IntegerField()
    url=models.FileField(upload_to='./upload/')
    def __str__(self):
        return self.url

class article_tag(models.Model):
    article_id=models.IntegerField()
    tag_name=models.CharField(max_length=30)
    def __str__(self):
        return self.tag_name

