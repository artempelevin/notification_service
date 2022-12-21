from django.db import models

from app.validators import phone_validator, mobile_operator_validator


class Client(models.Model):
    phone = models.CharField(max_length=11, validators=[phone_validator])
    mobile_operator = models.CharField(max_length=3, validators=[mobile_operator_validator])
    tag = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
