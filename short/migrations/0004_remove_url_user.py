# Generated by Django 4.1.2 on 2022-10-04 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0003_rename_user_id_url_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='user',
        ),
    ]
