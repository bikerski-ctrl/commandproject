# Generated by Django 5.0.6 on 2024-05-31 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_rename_task_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='media',
        ),
    ]