# Generated by Django 3.0 on 2019-12-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191217_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]