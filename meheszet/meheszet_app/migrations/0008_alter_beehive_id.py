# Generated by Django 4.0.5 on 2022-07-29 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meheszet_app', '0007_rename_quenbeecolor_beehive_queenbeecolor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beehive',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]