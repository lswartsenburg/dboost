from django.db import models

# Create your models here.
class TestObject(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
