from django.db import models
from django.contrib.auth.models import User


class Mascota(models.Model):
	nombre= models.CharField(max_length = 50)
	raza = models.CharField(max_length = 50)
	color = models.CharField(max_length = 30)
	imagen = models.ImageField(upload_to= 'mascotas', verbose_name= 'Imagen')
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

class Mascota_Perdida(models.Model):
	descripcion = models.TextField()
	recompensa = models.IntegerField()
	fecha= models.DateTimeField(auto_now=True)
	mascota = models.ForeignKey(Mascota)

	def __unicode__(self):
		return self.mascota.nombre

class Mascota_Encontrada(models.Model):
	foto = models.ImageField(upload_to = 'encontrados')
	raza= models.CharField(max_length = 30)
	color = models.CharField(max_length = 30)
	fecha_encontrada= models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)
	mascota = models.ForeignKey(Mascota)

	def __unicode__(self):
		return self.mascota.nombre	
	


# Create your models here.
