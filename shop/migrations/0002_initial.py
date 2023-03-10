# Generated by Django 4.1.2 on 2022-12-28 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='active_listing',
            name='add_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='active_listing',
            name='order_by',
            field=models.ManyToManyField(related_name='order_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
