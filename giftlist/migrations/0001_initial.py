# Generated by Django 4.2.17 on 2024-12-16 14:25

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
                ('giftlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('person_name', models.CharField(max_length=200)),
                ('budget', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giftlist_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('giftlist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giftlist', to='giftlist.giftlist')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
