# Generated by Django 3.0 on 2019-12-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pepper_app', '0009_remove_item_slugged_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slugged_title',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', editable=False),
        ),
    ]
