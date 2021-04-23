from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:modalidade_id>/modalidade', views.modalidade, name='modalidade'),
]