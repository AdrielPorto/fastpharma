from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('busca/', views.Busca, name='busca'),
    path('detalhe/<int:id>', views.Detalhe, name='detalhes'),

]
