# Generated by Django 3.1.1 on 2020-11-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20201110_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_student',
            name='Type_of_Hours',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
