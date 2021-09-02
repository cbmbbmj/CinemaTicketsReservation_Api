# Generated by Django 3.2.6 on 2021-09-02 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_type',
            field=models.CharField(choices=[('FT', 'FULL TIME'), ('PT', 'PART TIME')], default='FT', max_length=2),
        ),
    ]