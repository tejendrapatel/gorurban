# Generated by Django 3.2 on 2021-04-23 10:44

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0032_auto_20210423_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_procedures',
            name='cont',
            field=djrichtextfield.models.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='privacy_policys',
            name='cont',
            field=djrichtextfield.models.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='terms_conditionss',
            name='cont',
            field=djrichtextfield.models.RichTextField(null=True),
        ),
    ]