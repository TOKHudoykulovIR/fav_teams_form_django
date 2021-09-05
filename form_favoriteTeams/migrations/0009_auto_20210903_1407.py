# Generated by Django 3.2.6 on 2021-09-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_favoriteTeams', '0008_alter_generalinfo_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='favTeams',
            field=models.CharField(choices=[('MU', 'Manchester United'), ('MCI', 'Manchester City'), ('CHEL', 'Chelsea'), ('LIV', 'Liverpool'), ('ARS', 'Arsenal'), ('TOT', 'Tottenham'), ('BAY', 'Bayern Munich'), ('BVB', 'Borussia Dortmund'), ('RM', 'Real Madrid'), ('BAR', 'Barcelona'), ('ATM', 'Atletico Madrid'), ('JUV', 'Juventus'), ('INT', 'Inter'), ('ROMA', 'Roma'), ('NAP', 'Napoli'), ('ACM', 'Milan'), ('PSG', 'Paris Saint-Germain'), ('OL', 'Olympique Lyonnais'), ('LIL', 'Lille')], default=0, max_length=50, verbose_name='Team'),
        ),
        migrations.AddField(
            model_name='generalinfo',
            name='favTeamsLeague',
            field=models.CharField(choices=[('EPL', 'Premier League - England'), ('BUN', 'Bundesliga - Germany'), ('La L', 'La Liga - Spain'), ('Seria A', 'Serie A - Italy'), ('L1', 'Ligue 1 - France')], default=0, max_length=50, verbose_name='League'),
        ),
    ]
