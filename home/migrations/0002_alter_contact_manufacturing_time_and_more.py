# Generated by Django 4.2.5 on 2023-09-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Manufacturing_Time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Message',
            field=models.CharField(max_length=122),
        ),
    ]