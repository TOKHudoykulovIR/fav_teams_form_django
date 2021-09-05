from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import(
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)
from .models import GeneralInfo
from .forms import RawFavTeamForm



class FavTeamCreateView(CreateView):
	template_name = 'favteams/favteams_create.html'
	form_class = RawFavTeamForm
	queryset = GeneralInfo.objects.all()

	def form_valid(self, form):
		return super().form_valid(form)
		


