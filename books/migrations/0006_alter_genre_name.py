# Generated by Django 3.2.5 on 2021-07-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210720_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]