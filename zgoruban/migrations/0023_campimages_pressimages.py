# Generated by Django 3.1.7 on 2021-04-09 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0022_auto_20210409_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='campimages',
            name='pressimages',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
