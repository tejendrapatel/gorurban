# Generated by Django 3.1.7 on 2021-04-06 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0007_auto_20210406_0814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='about',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='about',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='about',
            name='image7',
        ),
    ]