from django.db import models

# Create your models here.
class  Post(models.Model):
    title=models.CharField(max_length=140)
    body=models.TextField(max_length=140)
    date=models.DateTimeField(auto_now_add=False)

def __str__ (self):
    return self.title