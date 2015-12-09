from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prueba.views.home', name='home'),
    # url(r'^prueba/', include('prueba.foo.urls')),
    url(r'^$', 'mascota.views.inicio'),
    url(r'^mascota/nueva/$','mascota.views.nueva_mascota'),
    url(r'^mascotas/$','mascota.views.lista_mascotas'),
    url(r'^mascotas_perdidas/$','mascota.views.mascotas_perdidas'),
    url(r'^mascotas_encontradas/$','mascota.views.mascotas_encontradas'),

    url(r'^mascota/(?P'mascota.nombre'\d+)$','mascota.views.detalle_mascota'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
)
