# Generated by Django 4.1.2 on 2022-10-04 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0010_url_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='user',
        ),
    ]
