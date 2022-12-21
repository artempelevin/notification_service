from django.db import models

from app.models import Mailing
from app.models.client import Client


class Message(models.Model):
    launch_at = models.DateTimeField()
    it_sent = models.BooleanField(default=False)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
