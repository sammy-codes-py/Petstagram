# Generated by Django 3.1.2 on 2020-10-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_remove_pet_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='details',
        ),
        migrations.AddField(
            model_name='like',
            name='test',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
    ]