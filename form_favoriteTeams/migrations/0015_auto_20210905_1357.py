# Generated by Django 3.2.6 on 2021-09-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_favoriteTeams', '0014_auto_20210904_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalinfo',
            name='gender',
            field=models.CharField(choices=[('', ''), ('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10, verbose_name='Jins*'),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='placeOfBirth',
            field=models.PositiveSmallIntegerField(choices=[('', ''), ('Andijon', 'Andijon viloyati'), ('Buxoro', 'Buxoro viloyati'), ('Jizzax', 'Jizzax viloyati'), ('Qashqadaryo', 'Qashqadaryo viloyati'), ('Navoiy', 'Navoiy viloyati'), ('Namangan', 'Namangan viloyati'), ('Samarqand', 'Samarqand viloyati'), ('Surxondaryo', 'Surxondaryo viloyati'), ('Sirdaryo', 'Sirdaryo viloyati'), ('Toshkent', 'Toshkent viloyati'), ('Fargʻona', 'Fargʻona viloyati'), ('Xorazm', 'Xorazm viloyati'), ('Qoraqalpogʻiston', 'Qoraqalpogʻiston Respublikasi')], verbose_name="Tug'ilgan Joyi*"),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='placeOfResidence',
            field=models.PositiveSmallIntegerField(choices=[('', ''), ('Andijon', 'Andijon viloyati'), ('Buxoro', 'Buxoro viloyati'), ('Jizzax', 'Jizzax viloyati'), ('Qashqadaryo', 'Qashqadaryo viloyati'), ('Navoiy', 'Navoiy viloyati'), ('Namangan', 'Namangan viloyati'), ('Samarqand', 'Samarqand viloyati'), ('Surxondaryo', 'Surxondaryo viloyati'), ('Sirdaryo', 'Sirdaryo viloyati'), ('Toshkent', 'Toshkent viloyati'), ('Fargʻona', 'Fargʻona viloyati'), ('Xorazm', 'Xorazm viloyati'), ('Qoraqalpogʻiston', 'Qoraqalpogʻiston Respublikasi')], verbose_name='Yashash Joyi*'),
        ),
    ]
