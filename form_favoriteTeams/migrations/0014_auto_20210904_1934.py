# Generated by Django 3.2.6 on 2021-09-04 14:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_favoriteTeams', '0013_auto_20210904_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(75)], verbose_name='Yosh*'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='favTeams',
            field=models.CharField(choices=[('', ''), ('ARS', 'Arsenal'), ('CHEL', 'Chelsea'), ('LIV', 'Liverpool'), ('MU', 'Manchester United'), ('MCI', 'Manchester City'), ('TOT', 'Tottenham'), ('BAY', 'Bayern Munich'), ('BVB', 'Borussia Dortmund'), ('ATM', 'Atletico Madrid'), ('BAR', 'Barcelona'), ('RM', 'Real Madrid'), ('JUV', 'Juventus'), ('INT', 'Inter'), ('ROMA', 'Roma'), ('NAP', 'Napoli'), ('ACM', 'Milan'), ('PSG', 'Paris Saint-Germain'), ('OL', 'Olympique Lyonnais'), ('LIL', 'Lille')], max_length=50, verbose_name='Jamoa*'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='gender',
            field=models.CharField(choices=[('', ''), ('M', 'Erkak'), ('F', 'Ayol')], max_length=1, verbose_name='Jins*'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='placeOfBirth',
            field=models.PositiveSmallIntegerField(choices=[('', ''), (1, 'Andijon viloyati'), (2, 'Buxoro viloyati'), (3, 'Jizzax viloyati'), (4, 'Qashqadaryo viloyati'), (5, 'Navoiy viloyati'), (6, 'Namangan viloyati'), (7, 'Samarqand viloyati'), (8, 'Surxondaryo viloyati'), (9, 'Sirdaryo viloyati'), (10, 'Toshkent viloyati'), (11, 'Fargʻona viloyati'), (12, 'Xorazm viloyati'), (13, 'Qoraqalpogʻiston Respublikasi')], verbose_name="Tug'ilgan Joyi*"),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='placeOfResidence',
            field=models.PositiveSmallIntegerField(choices=[('', ''), (1, 'Andijon viloyati'), (2, 'Buxoro viloyati'), (3, 'Jizzax viloyati'), (4, 'Qashqadaryo viloyati'), (5, 'Navoiy viloyati'), (6, 'Namangan viloyati'), (7, 'Samarqand viloyati'), (8, 'Surxondaryo viloyati'), (9, 'Sirdaryo viloyati'), (10, 'Toshkent viloyati'), (11, 'Fargʻona viloyati'), (12, 'Xorazm viloyati'), (13, 'Qoraqalpogʻiston Respublikasi')], verbose_name='Yashash Joyi*'),
        ),
    ]
