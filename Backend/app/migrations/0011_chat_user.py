# Generated by Django 4.0.2 on 2022-04-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_chat_chatbot_remove_chat_chatbot_messages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]