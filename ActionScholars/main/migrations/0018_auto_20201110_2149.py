# Generated by Django 3.1.1 on 2020-11-11 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20201110_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_student',
            name='Status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Denied', 'Denied')], default='Pending', max_length=30),
        ),
    ]
