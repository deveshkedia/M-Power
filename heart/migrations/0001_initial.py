# Generated by Django 4.0.3 on 2022-07-16 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0007_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartCancerText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmi', models.DecimalField(decimal_places=3, max_digits=5)),
                ('smoking', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('alcohol', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('stroke', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('diff_walking', models.CharField(choices=[(1, 'Yes'), (0, 'No')], max_length=255)),
                ('gender', models.CharField(choices=[(1, 'Male'), (0, 'Female')], max_length=255)),
                ('age_category', models.IntegerField(choices=[(0, '18-24'), (1, '25-29'), (2, '30-34'), (3, '35-39'), (4, '40-44'), (5, '45-49'), (6, '50-54'), (7, '55-59'), (8, '60-64'), (9, '65-69'), (10, '70-74'), (11, '75-79'), (12, '80 or older)')])),
                ('race', models.IntegerField(choices=[(0, 'American Indian/Alaskan Native'), (1, 'Asian'), (2, 'Black'), (3, 'Hispanic'), (4, 'Other'), (5, 'White')])),
                ('diabetic', models.IntegerField(choices=[(0, 'No'), (1, 'No, borderline diabetes'), (2, 'Yes'), (3, 'Yes (during pregnancy)')])),
                ('gen_health', models.IntegerField(choices=[(0, 'Excellent'), (1, 'Fair'), (2, 'Good'), (3, 'Poor'), (4, 'Very good')])),
                ('sleep_time', models.DecimalField(decimal_places=3, max_digits=5)),
                ('physical_activity', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('asthma', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('kidney_disease', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('skin_cancer', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='HeartReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('result', models.TextField(blank=True, null=True)),
                ('data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='heart.heartcancertext')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
    ]
