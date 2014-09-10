from datetime import time, timedelta
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class DurationField(models.Field):
    description = "makes field from time class to time database type "
    __metaclass__=models.SubfieldBase

    def __init__(self,help_text=("A comma-separated latitude longitude pair"),verbose_name='durationfield', *args,**kwargs):
        self.name="DurationField",
        self.through = None
        self.help_text = help_text
        self.blank = True
        self.editable = True
        self.creates_table = False
        self.db_column = None
        self.serialize = False
        self.null = True
        self.creation_counter = models.Field.creation_counter
        models.Field.creation_counter += 1
        super(DurationField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'time'

    def to_python(self, value):
        if value in ( None,''):
            return DurationField()
        else:
            if isinstance(value, time):
                return (timedelta(hours=value.hour, minutes=value.minute, seconds=value.second))
            else:
                args = [int(value.split(':')[0]),int(value.split(':')[1]), int(value.split(':')[2])]
                if len(args) != 3 and value is not None:
                    raise ValidationError("Invalid input for a GeoCoordinate instance")
                return time(*args)

    def get_prep_value(self, value):
        return ':'.join([str(value.hour),str(value.minute),str(value.second)])


class Product(models.Model):
    name = models.CharField(max_length=20, blank=False, help_text="product's model and some details")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.ForeignKey(User)
    na_prodaje = models.BooleanField(default=False)
    time = DurationField()


    def __unicode__(self):
        return  u'%s %s' % (self.name, self.time)


class Duration(object):
    def __init__(self, hour, minute, second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __repr__(self):
        return str(self.hour)+':'+str(self.minute)+':'+str(self.second)




