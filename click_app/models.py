from datetime import time, timedelta
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from datetime import datetime

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s" % filename

class Product(models.Model):
    name = models.CharField(max_length=20, blank=False, help_text="product's model and some details")
    image = models.FileField(upload_to=get_upload_file_name)
    time = models.TimeField()

    expiration_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.ForeignKey(User, default=None)
    na_prodaje = models.BooleanField(default=False)

    def now_na_prodaje(self):
        return  datetime.now() > self.expiration_date

    def __unicode__(self):
        return  u'%s %s' % (self.name, self.time)





