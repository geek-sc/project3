# Generated by Django 2.0.3 on 2019-02-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20190214_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='extra',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]