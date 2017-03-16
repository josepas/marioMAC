

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_preguntas'),
    url(r'^(?P<id>\d{1,50})/$', views.pregunta, name='pregunta'),
]