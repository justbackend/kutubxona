# Generated by Django 4.2.5 on 2023-09-10 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muallif',
            name='tirik',
            field=models.BooleanField(default=True),
        ),
    ]
