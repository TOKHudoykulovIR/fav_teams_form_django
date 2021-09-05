from django import forms
from .models import GeneralInfo

class RawFavTeamForm(forms.ModelForm):
	class Meta:
		model=GeneralInfo
		fields='__all__'

		GENDER = [
			('', ''),
			('Erkak', "Erkak"),
			('Ayol', "Ayol")
		]

		REGIONS = [
			('', ''),
			(1, 'Andijon viloyati'),
			(2, 'Buxoro viloyati'),
			(3, 'Jizzax viloyati'),
			(4, 'Qashqadaryo viloyati'),
			(5, 'Navoiy viloyati'),
			(6, 'Namangan viloyati'),
			(7, 'Samarqand viloyati'),
			(8, 'Surxondaryo viloyati'),
			(9, 'Sirdaryo viloyati'),
			(10, 'Toshkent viloyati'),
			(11, 'Fargʻona viloyati'),
			(12, 'Xorazm viloyati'),
			(13, 'Qoraqalpogʻiston Respublikasi')
		]

		LEAGUES = [
			('', ''),
			('EPL', 'Premier League - England'),
			('BUN', 'Bundesliga - Germany'),
			('La L', 'La Liga - Spain'), 
			('Seria A', 'Serie A - Italy'),
			('L1', 'Ligue 1 - France')
		]

		TEAMS = [
			('', ''),
			('ARS', 'Arsenal'),
			('CHEL', 'Chelsea'),
			('LIV', 'Liverpool'),
			('MU', 'Manchester United'),
			('MCI', 'Manchester City'),   
			('TOT', 'Tottenham'), 
			('BAY', 'Bayern Munich'),
			('BVB', 'Borussia Dortmund'),
			('ATM', 'Atletico Madrid'),
			('BAR', 'Barcelona'),
			('RM', 'Real Madrid'),
			('JUV', 'Juventus'),
			('INT', 'Inter'),
			('ROMA', 'Roma'),
			('NAP', 'Napoli'),
			('ACM', 'Milan'),
			('PSG', 'Paris Saint-Germain'),
			('OL', 'Olympique Lyonnais'),
			('LIL', 'Lille')
		]

		widgets = {
			'name' : forms.TextInput(attrs = {'class' : 'form_input'}),
			'surname':forms.TextInput(attrs = {'class' : 'form_input'}),
			'age' : forms.TextInput(attrs = {'class' : 'form_input'}),
			'gender': forms.Select(choices=GENDER, attrs={'class' : 'form_input'}),
			'placeOfBirth': forms.Select(choices=REGIONS, attrs={'class': 'form_input'}),
			'placeOfResidence': forms.Select(choices=REGIONS, attrs={'class': 'form_input'}),
			'favTeamsLeague': forms.Select(choices=LEAGUES, attrs={'class': 'form_input'}),
			'favTeams': forms.Select(choices=TEAMS, attrs={'class': 'form_input'})
		}
