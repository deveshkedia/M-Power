# Generated by Django 4.0.3 on 2022-07-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(blank=True, default='defaults/profile.svg', upload_to='profile/'),
        ),
    ]