
from django.urls import path
from app_cad_aluno import views

urlpatterns = [
    # aqui vai rota, view ,  nome referencia
    path('',views.home, name='home'),
    # rota para lista de alunos
    path('alunos/', views.alunos, name='lista_alunos')
]
