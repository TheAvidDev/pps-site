# Generated by Django 2.2.5 on 2019-12-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20191218_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='banner',
            field=models.CharField(blank=True, default=None, help_text="A banner showed on the Category's page.", max_length=1000, null=True),
        ),
    ]
