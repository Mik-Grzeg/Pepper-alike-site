# Generated by Django 3.0 on 2019-12-10 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pepper_app', '0006_auto_20191207_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pepper_app.Subcategory'),
        ),
    ]
