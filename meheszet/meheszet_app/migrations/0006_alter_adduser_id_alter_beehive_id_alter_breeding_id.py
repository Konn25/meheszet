# Generated by Django 4.0.5 on 2022-07-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meheszet_app', '0005_alter_beehive_beehivestrength_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='beehive',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='breeding',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
