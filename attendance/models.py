from django.db import models
from django.contrib.auth.models import User

class Punch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    punch_in_time = models.DateTimeField()
    punch_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.punch_in_time} - {self.punch_out_time}"

class UserLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)