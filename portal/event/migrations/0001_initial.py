# Generated by Django 5.0.6 on 2024-05-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=150)),
                ('time', models.DateTimeField()),
                ('date', models.DateField()),
            ],
        ),
    ]