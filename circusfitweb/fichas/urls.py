from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homefichas'),
    path('<int:modalidade_id>/modalidade', views.modalidade, name='modalidade'),
    path('modalidades/', views.modalidades, name='modalidades'),
]