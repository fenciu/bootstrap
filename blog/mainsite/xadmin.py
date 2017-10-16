import xadmin
from .models import article,article_pic,article_tag
xadmin.site.register([article,article_pic,article_tag])