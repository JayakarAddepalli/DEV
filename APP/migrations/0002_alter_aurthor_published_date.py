# Generated by Django 5.0.7 on 2024-08-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aurthor',
            name='published_date',
            field=models.DateField(auto_created=True),
        ),
    ]