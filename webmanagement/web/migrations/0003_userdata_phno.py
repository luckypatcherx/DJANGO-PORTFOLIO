# Generated by Django 4.1.8 on 2023-04-09 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='phno',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]