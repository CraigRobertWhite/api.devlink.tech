# Generated by Django 3.1.9 on 2021-05-06 05:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0005_auto_20210504_0434'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyposition',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]
