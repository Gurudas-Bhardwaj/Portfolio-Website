# Generated by Django 5.0.6 on 2024-06-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Message',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='Number',
            field=models.CharField(max_length=20),
        ),
    ]
