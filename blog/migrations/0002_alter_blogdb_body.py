# Generated by Django 3.2.6 on 2021-09-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdb',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]
