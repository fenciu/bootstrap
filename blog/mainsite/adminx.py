import xadmin
from .models import article
class articleAdmin(object):
    print("start")
xadmin.site.register(article,articleAdmin)