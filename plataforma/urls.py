from django.urls import path
from . import views

urlpatterns = [
    path('logar/', views.logar, name='logar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.plataforma, name='plataforma'),
    path('logout', views.logout_view, name='logout_view'),
    path('cadastro_nota', views.cadastro_nota, name='cadastro_nota')
]
