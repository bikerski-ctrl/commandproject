# Generated by Django 5.0.6 on 2024-05-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum_theme',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]