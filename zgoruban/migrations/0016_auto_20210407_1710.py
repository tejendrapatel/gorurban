# Generated by Django 3.1.7 on 2021-04-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0015_auto_20210407_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='Year',
            field=models.CharField(choices=[('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')], default='2021', max_length=30),
        ),
    ]
