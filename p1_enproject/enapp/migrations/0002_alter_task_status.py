# Generated by Django 5.1 on 2024-08-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='Pending', max_length=10),
        ),
    ]
