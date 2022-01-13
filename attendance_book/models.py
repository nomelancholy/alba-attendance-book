from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=5)
    birthdate = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=4)