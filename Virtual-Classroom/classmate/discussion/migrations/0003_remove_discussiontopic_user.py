# Generated by Django 5.0.4 on 2024-05-04 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0002_discussiontopic_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussiontopic',
            name='user',
        ),
    ]
