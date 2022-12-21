# Generated by Django 4.1.4 on 2022-12-21 19:04

import app.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, validators=[app.validators.phone_validator])),
                ('mobile_operator', models.CharField(max_length=3, validators=[app.validators.mobile_operator_validator])),
                ('tag', models.CharField(max_length=50)),
                ('time_zone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_at', models.DateTimeField()),
                ('text', models.CharField(max_length=160)),
                ('client_tag', models.CharField(max_length=50)),
                ('mobile_operator', models.CharField(max_length=3, validators=[app.validators.mobile_operator_validator])),
                ('finish_in', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_at', models.DateTimeField()),
                ('it_sent', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.mailing')),
            ],
        ),
    ]