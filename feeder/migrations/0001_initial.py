# Generated by Django 2.2.4 on 2019-09-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('img', models.URLField(max_length=250)),
                ('url', models.URLField(max_length=250)),
            ],
        ),
    ]
