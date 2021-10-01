# Generated by Django 3.1.7 on 2021-04-05 16:07

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0002_go_ruban_motive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_name', models.CharField(max_length=30, null=True)),
                ('no_of_days', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('content', djrichtextfield.models.RichTextField(null=True)),
            ],
        ),
    ]