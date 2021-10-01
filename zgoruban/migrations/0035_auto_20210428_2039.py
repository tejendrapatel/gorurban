# Generated by Django 3.2 on 2021-04-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0034_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]