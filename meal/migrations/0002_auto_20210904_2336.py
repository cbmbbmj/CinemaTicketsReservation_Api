# Generated by Django 3.2.7 on 2021-09-04 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'meal')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('user', 'meal')},
        ),
    ]
