# Generated by Django 4.2.17 on 2024-12-16 16:05

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
            name='GiftList',
            fields=[
                ('giftlistID', models.AutoField(primary_key=True, serialize=False)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giftlist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
