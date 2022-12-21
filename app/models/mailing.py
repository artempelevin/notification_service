from django.db import models

from app.validators import mobile_operator_validator


class Mailing(models.Model):
    launch_at = models.DateTimeField()
    text = models.CharField(max_length=160)
    client_tag = models.CharField(max_length=50)
    mobile_operator = models.CharField(max_length=3, validators=[mobile_operator_validator])
    finish_in = models.DateTimeField()
