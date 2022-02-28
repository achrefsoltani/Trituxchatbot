# Generated by Django 4.0.2 on 2022-02-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_choice_next_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='title',
        ),
        migrations.AddField(
            model_name='choice',
            name='title_en',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='title_fr',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='response_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='response_fr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]