# Generated by Django 4.0.3 on 2022-07-21 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0007_alter_lungreport_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='lungreport',
            name='image_data',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cancer.lungcancerimage'),
        ),
    ]
