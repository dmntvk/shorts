# Generated by Django 4.1.2 on 2022-10-04 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0007_url_abobys'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='user',
            new_name='users_id',
        ),
    ]