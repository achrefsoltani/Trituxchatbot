# Generated by Django 4.0.2 on 2022-06-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_demorequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(blank=True, choices=[('service1', 'service 1'), ('service2', 'service2'), ('service3', 'service 3')], max_length=20)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('event_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
