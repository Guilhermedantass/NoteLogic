from django.urls import path
from . import views

urlpatterns = [
    path('logar/', views.logar, name='logar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.plataforma, name='plataforma'),
    path('logout', views.logout_view, name='logout_view'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task', views.delete_task, name='delete_task'),
    path('done_task', views.done_task, name='done_task'),
    path('undone_task', views.undone_task, name='undone_task')
]
