# Generated by Django 3.1.7 on 2021-04-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Go_Ruban_Motive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motive', models.TextField(null=True)),
            ],
        ),
    ]
