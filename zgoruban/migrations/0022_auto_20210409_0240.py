# Generated by Django 3.1.7 on 2021-04-09 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zgoruban', '0021_blogimages_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='CAMPimages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(null=True, upload_to='')),
                ('imag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zgoruban.camps')),
            ],
        ),
        migrations.DeleteModel(
            name='Blogimages',
        ),
    ]
