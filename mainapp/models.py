from django.db import models
from django.forms import MultiValueField


# Create your models her

class contact(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    looking_for = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class SubscriptionEmail(models.Model):
    subemail = models.EmailField()

    def __str__(self):
        return self.subemail
