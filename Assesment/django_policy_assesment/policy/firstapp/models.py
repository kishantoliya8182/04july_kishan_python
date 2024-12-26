from django.db import models

# Create your models here.
class signup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    mail=models.EmailField()
