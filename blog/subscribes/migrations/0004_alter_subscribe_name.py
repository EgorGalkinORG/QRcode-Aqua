# Generated by Django 5.1.2 on 2025-02-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribes', '0003_remove_subscribe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
