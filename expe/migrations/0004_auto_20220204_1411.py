# Generated by Django 3.2.12 on 2022-02-04 14:11

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('expe', '0003_auto_20220204_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplepage',
            name='javascripts',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('example.js', 'static/experiment/js/example.js')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='examplepage',
            name='styles',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('example.css', 'static/experiment/css/example.css')], max_length=11, null=True),
        ),
    ]
