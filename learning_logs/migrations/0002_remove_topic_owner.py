# Generated by Django 3.0.8 on 2020-07-26 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='owner',
        ),
    ]
