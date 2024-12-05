# Generated by Django 5.1.3 on 2024-12-05 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.cat'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(),
        ),
    ]
