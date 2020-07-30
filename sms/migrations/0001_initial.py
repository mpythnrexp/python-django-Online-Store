# Generated by Django 3.0.7 on 2020-07-30 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.BooleanField(default=False, editable=False, null=True)),
                ('message_text', models.CharField(editable=False, max_length=160, null=True)),
                ('africastalking_response', models.CharField(editable=False, max_length=255, null=True)),
                ('time_sent', models.DateTimeField(editable=False, null=True)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now_add=True)),
                ('sent_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['time_last_edited'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(editable=False, max_length=255)),
                ('status_code', models.CharField(editable=False, max_length=255)),
                ('cost', models.CharField(editable=False, max_length=255)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('message_info', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='sms.SmsInfo')),
            ],
        ),
    ]
