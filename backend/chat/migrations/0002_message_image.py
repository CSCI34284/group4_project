# Generated by Django 2.2.7 on 2019-11-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.BooleanField(default=False),
        ),
    ]
