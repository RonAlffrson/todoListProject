# Generated by Django 4.2.7 on 2024-02-07 20:11

from django.db import migrations, models
import todoapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_todolistitem_created_date_todolistitem_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='due_date',
            field=models.DateTimeField(blank=True, default=todoapp.models.one_week_hence),
        ),
    ]
