from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class GeneralInfo(models.Model):

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

	name 			 = models.CharField('Ism', max_length = 50, blank = True)
	surname 		 = models.CharField('Familiya', max_length = 50, blank = True)
	age				 = models.PositiveIntegerField('Yosh*', validators = [MinValueValidator(5), MaxValueValidator(75)])
	gender			 = models.CharField('Jins*', max_length = 10, choices = GENDER)
	placeOfBirth 	 = models.PositiveSmallIntegerField("Tug'ilgan Joyi*", choices = REGIONS)
	placeOfResidence = models.PositiveSmallIntegerField('Yashash Joyi*', choices = REGIONS)
	#favTeamsLeague	 = models.CharField('League', max_length = 50, choices = LEAGUES)
	favTeams 		 = models.CharField('Jamoa*', max_length = 50, choices = TEAMS)


	def get_absolute_url(self):
		return reverse('form_favoriteTeams:create_form')   #f"/product/{self.id}/" - another method

	

