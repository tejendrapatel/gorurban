# Generated by Django 3.2.7 on 2021-10-01 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0050_auto_20210920_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryss',
            name='image2',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]