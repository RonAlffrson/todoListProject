# Generated by Django 4.2.7 on 2024-02-08 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_alter_todolistitem_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 14, 17, 32, 658273, tzinfo=datetime.timezone.utc)),
        ),
    ]
