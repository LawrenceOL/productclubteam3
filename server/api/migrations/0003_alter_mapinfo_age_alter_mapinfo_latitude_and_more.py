# Generated by Django 4.0.6 on 2022-08-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_mapinfo_apartments_alter_mapinfo_census_tract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapinfo',
            name='age',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mapinfo',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mapinfo',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mapinfo',
            name='neighbor_mapping',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mapinfo',
            name='neighborhood_code',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mapinfo',
            name='property_class',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mapinfo',
            name='town_and_neighbor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mapinfo',
            name='town_code',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]