# Generated by Django 2.2 on 2019-04-06 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labsection',
            name='section_number',
            field=models.IntegerField(),
        ),
    ]
