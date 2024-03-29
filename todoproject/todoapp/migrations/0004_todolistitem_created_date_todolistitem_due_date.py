# Generated by Django 4.2.7 on 2024-02-06 13:36

from django.db import migrations, models
import django.utils.timezone
import todoapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_rename_name_todolistitem_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todolistitem',
            name='due_date',
            field=models.DateTimeField(default=todoapp.models.one_week_hence),
        ),
    ]
