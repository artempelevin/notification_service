from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app.models import Client, Message, Mailing


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    pass


@admin.register(Mailing)
class MailingAdmin(ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    pass
