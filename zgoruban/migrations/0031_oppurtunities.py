# Generated by Django 3.1.7 on 2021-04-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0030_news_letter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oppurtunities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('mob', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('role', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]