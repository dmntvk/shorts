# Generated by Django 4.1.2 on 2022-10-04 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0008_rename_user_url_users_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='abobys',
        ),
        migrations.RemoveField(
            model_name='url',
            name='users_id',
        ),
    ]
