# Generated by Django 4.2.4 on 2023-11-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
