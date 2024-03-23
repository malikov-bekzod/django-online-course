# Generated by Django 5.0.3 on 2024-03-23 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_teacher_instagram_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='instagram_link',
            field=models.URLField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='linkedin_link',
            field=models.URLField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='telegram_link',
            field=models.URLField(max_length=250, null=True),
        ),
    ]
