# Generated by Django 4.0.3 on 2022-03-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]