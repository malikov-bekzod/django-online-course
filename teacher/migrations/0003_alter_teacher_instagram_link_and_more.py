# Generated by Django 5.0.3 on 2024-03-23 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_speciality_alter_teacher_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='instagram_link',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='linkedin_link',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='telegram_link',
            field=models.CharField(max_length=250, null=True),
        ),
    ]