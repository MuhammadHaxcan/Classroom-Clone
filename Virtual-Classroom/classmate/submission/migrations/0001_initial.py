# Generated by Django 5.0.4 on 2024-05-02 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0002_alter_classroom_options_assignment_file_and_more'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='submissions/')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userprofile')),
            ],
        ),
    ]
