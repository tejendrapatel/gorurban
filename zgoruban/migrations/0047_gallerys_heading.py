# Generated by Django 3.2.7 on 2021-09-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0046_auto_20210920_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerys',
            name='Heading',
            field=models.TextField(max_length=150, null=True),
        ),
    ]
