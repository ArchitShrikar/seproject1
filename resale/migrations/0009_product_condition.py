# Generated by Django 3.2 on 2021-05-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0008_auto_20210504_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(default='Good', max_length=255),
        ),
    ]
