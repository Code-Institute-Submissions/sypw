from django.db import models
# from profiles.models import UserProfile
# from checkout.models import Order
from django.contrib.auth.models import User


# parent model
class Forum(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, null=False, default=User)
    topic = models.CharField(max_length=300, null=False)
    description = models.CharField(max_length=1000, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.topic)


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(Forum, blank=False, on_delete=models.CASCADE)
    discuss = models.TextField(max_length=1200)
    nick = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.forum)
