# Generated by Django 3.1.7 on 2021-04-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210412_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.FilePathField(path='/projects/static/img/'),
        ),
    ]
