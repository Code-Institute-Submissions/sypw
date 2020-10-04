from django.db import models
from profiles.models import UserProfile
from checkout.models import Order
from django.contrib.auth.models import User


# parent model
class forum(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, default=UserProfile)
    email = models.CharField(max_length=200, null=True, default=Order)
    topic = models.CharField(max_length=300, null=False)
    description = models.CharField(max_length=1000, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return str(self.topic)


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE)
    discuss = models.TextField(max_length=1200)
    nick = models.CharField(max_length=200, default=User)

    def __str__(self):
        return str(self.forum)
