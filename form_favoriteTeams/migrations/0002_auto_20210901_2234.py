# Generated by Django 3.2.6 on 2021-09-01 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_favoriteTeams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='placeOfBirth',
            field=models.PositiveSmallIntegerField(choices=[(0, 'NaN'), (1, 'Andijan region'), (2, 'Bukhara region'), (3, 'Jizzakh region'), (4, 'Kashkadarya region'), (5, 'Navoi region'), (6, 'Namangan region'), (7, 'Samarkand region'), (8, 'Surkhandarya region'), (9, 'Syrdarya region'), (10, 'Tashkent region'), (11, 'Tashkent city'), (12, 'Fergana region'), (13, 'Khorezm region'), (14, 'Republic of Karakalpakstan')], default=0),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='placeOfResidence',
            field=models.PositiveSmallIntegerField(choices=[(0, 'NaN'), (1, 'Andijan region'), (2, 'Bukhara region'), (3, 'Jizzakh region'), (4, 'Kashkadarya region'), (5, 'Navoi region'), (6, 'Namangan region'), (7, 'Samarkand region'), (8, 'Surkhandarya region'), (9, 'Syrdarya region'), (10, 'Tashkent region'), (11, 'Tashkent city'), (12, 'Fergana region'), (13, 'Khorezm region'), (14, 'Republic of Karakalpakstan')], default=0),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='gender',
            field=models.CharField(choices=[('М', 'Мужик'), ('Ж', 'Женщина')], max_length=1),
        ),
    ]