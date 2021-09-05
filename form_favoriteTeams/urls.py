from django.urls import path
from form_favoriteTeams.views import (
	FavTeamCreateView,
	)

app_name = 'form_favoriteTeams'
urlpatterns = [
	path('', FavTeamCreateView.as_view(), name = 'create_form'),
]