from django import forms

from .models import ProjectTitle

class FormProjectTitle(forms.ModelForm):
	class Meta:
		model = ProjectTitle
		fields = ['title', 'location', 'contact_email', 'description', 'team_members']


	def clean_title(self):
		title = self.cleaned_data.get('title')
		return title

	def clean_description(self):
		description = self.cleaned_data.get('description')
		return description

	def clean_location(self):
		location = self.cleaned_data.get('location')
		return location

	def clean_title(self):
		team_members = self.cleaned_data.get('team_members')
		return team_members

	