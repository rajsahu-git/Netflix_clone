# Generated by Django 4.0.2 on 2022-02-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='age_limit',
            field=models.CharField(choices=[('ALL', 'ALL'), ('Kids', 'Kids')], max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age_limit',
            field=models.CharField(choices=[('ALL', 'ALL'), ('Kids', 'Kids')], max_length=10),
        ),
    ]