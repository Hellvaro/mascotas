#encoding: utf-8
from django.forms import ModelForm
from django import forms
from mascota.models import Mascota

class MascotaForm(ModelForm):
	class Meta:
		model = Mascota