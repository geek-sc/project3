# Generated by Django 2.0.3 on 2019-02-09 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190208_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_regular_pizza',
            name='idname',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
