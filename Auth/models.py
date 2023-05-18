from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    date_joined = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
       return str(self.name)
