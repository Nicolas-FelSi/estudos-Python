from django.urls import path
from . views import cadastrar_tarefa, listar_tarefas


urlpatterns = [
    path('cadastrar_tarefa/', cadastrar_tarefa, name='cadastrar_tarefa'),
    path('lista_tarefas/', listar_tarefas, name='lista_tarefas')
]