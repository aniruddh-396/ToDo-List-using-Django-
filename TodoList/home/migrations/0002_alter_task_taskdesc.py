# Generated by Django 4.1.7 on 2023-04-08 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskDesc',
            field=models.TextField(),
        ),
    ]