# Generated by Django 5.0.4 on 2024-05-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_alter_classroom_options_assignment_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
