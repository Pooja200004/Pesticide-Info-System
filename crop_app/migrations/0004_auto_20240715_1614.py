# Generated by Django 3.2.25 on 2024-07-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop_app', '0003_auto_20240712_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otpcode',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='otpcode',
            name='status',
        ),
        migrations.AddField(
            model_name='otpcode',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='otpcode',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='otpcode',
            name='utype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
