# Generated by Django 4.2.14 on 2025-01-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0009_rename_topic_info_topicmodel_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTMLBlogsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topics', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HTMLTopicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]