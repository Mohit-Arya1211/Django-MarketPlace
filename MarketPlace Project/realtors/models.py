from datetime import datetime
from django.db import models

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    describe = models.TextField(blank=True)
    phone = models.IntegerField()
    email = models.CharField(max_length=100, blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name