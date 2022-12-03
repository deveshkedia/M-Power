# Generated by Django 4.0.3 on 2022-07-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='blood_group',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doctor_number',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='emergency_contact',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
