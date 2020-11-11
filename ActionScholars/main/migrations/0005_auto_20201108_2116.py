# Generated by Django 3.1.1 on 2020-11-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201108_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_student',
            old_name='Approved',
            new_name='Status',
        ),
        migrations.AddField(
            model_name='event_student',
            name='Hours',
            field=models.CharField(choices=[('Required', 'Required'), ('Active', 'Active'), ('Receptive', 'Receptive')], max_length=30, null=True),
        ),
    ]