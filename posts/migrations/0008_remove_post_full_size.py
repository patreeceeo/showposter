# Generated by Django 3.0.3 on 2020-02-20 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200211_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='full_size',
        ),
    ]