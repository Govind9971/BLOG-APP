# Generated by Django 3.1.3 on 2020-12-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poko', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
