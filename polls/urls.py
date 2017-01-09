from django.conf.urls import include, url
from . import views

urlpatterns = [

	#Listas
	url(r'^$', views.post_list),

	#Detalles
	url(r'^polls/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),


	#Anyadido
	url(r'^polls/new', views.post_new, name='post_new'),

	#Modificado
	url(r'^polls/(?P<post_id>\d+)/edit/$', views.post_edit, name='post_edit'),

	#Borrado
	url(r'^polls/(?P<post_id>\d+)/delete/$', views.post_delete, name='post_delete'),

	#Contacto
	url(r'^polls/contacto/$', views.post_contacto, name='post_contacto'),
]
