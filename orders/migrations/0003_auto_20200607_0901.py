# Generated by Django 3.0.7 on 2020-06-07 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='time_added',
        ),
        migrations.RemoveField(
            model_name='order',
            name='time_last_edited',
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
