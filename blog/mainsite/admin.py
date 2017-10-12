from django.contrib import admin
from .models import article,article_pic,article_tag
# Register your models here.
admin.site.register([article,article_pic,article_tag])
