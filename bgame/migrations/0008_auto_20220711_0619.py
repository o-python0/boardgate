# Generated by Django 3.2.13 on 2022-07-11 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bgame', '0007_auto_20220706_2100'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='wantplay',
            name='wantplay_unique',
        ),
        migrations.AlterField(
            model_name='wantplay',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wantplay_user', to=settings.AUTH_USER_MODEL),
        ),
    ]