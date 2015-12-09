# Create your views here.
from mascota.models import Mascota,Mascota_Perdida, Mascota_Encontrada
from mascota.forms import MascotaForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def lista_mascotas(request):
	mascotas=Mascota.objects.all()
	return render_to_response('mascotas.html',{'datos': mascotas}, context_instance=RequestContext(request))

def detalle_mascota(request, id_mascota):
		dato = get_object_or_404(Mascota , pk=id_mascota)
		return render_to_response('mascota.html',{'mascota':dato}, context_instance=RequestContext(request))

def inicio(request):
		mascotas = Mascota.objects.all()
		return render_to_response('inicio.html',{'mascotas': mascotas})		


def nueva_mascota(request):
	if request.method == 'POST':
		formulario = MascotaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/mascotas')
	else:
		formulario = MascotaForm()
	return render_to_response('mascotaform.html',{'formulario':formulario}, context_instance = RequestContext(request))			

def mascotas_perdidas(request):
	mascotas = Mascota_Perdida.objects.all()
	return render_to_response('mascotas_perdidas.html',{'datos':mascotas}, context_instance=RequestContext(request))

def mascotas_encontradas(request):
	mascotas = Mascota_Encontrada.objects.all()
	return render_to_response('mascotas_encontradas.html',{'datos':mascotas}, context_instance=RequestContext(request))
