# Generated by Django 4.0.2 on 2022-05-30 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_alter_contactrequest_agent_alter_contactrequest_chat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactrequest',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
