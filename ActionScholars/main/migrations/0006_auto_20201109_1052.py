# Generated by Django 3.1.1 on 2020-11-09 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201108_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_student',
            old_name='Hours',
            new_name='Type_of_Hours',
        ),
    ]
