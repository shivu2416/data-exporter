# Generated by Django 4.2.4 on 2023-08-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_exporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
