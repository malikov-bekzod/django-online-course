# Generated by Django 5.0.3 on 2024-03-23 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='course.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
