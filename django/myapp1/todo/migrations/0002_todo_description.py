# Generated by Django 5.0.6 on 2024-06-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
