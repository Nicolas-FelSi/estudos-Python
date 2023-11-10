from django.shortcuts import render, redirect
from . forms import TarefaForm
from . models import Tarefa


def cadastrar_tarefa(request):
    if request.method == 'POST':
        tarefa_form = TarefaForm(request.POST)
        if tarefa_form.is_valid():
            tarefa_form.save()
        return redirect('lista_tarefas')
    else:   
        tarefa_form = TarefaForm()
    return render(request, 'form_cadastro.html', {'form_tarefa': tarefa_form})


def listar_tarefas(request):
    tarefa = Tarefa.objects.all()
    return render(request, 'lista_tarefas.html', {'tarefa': tarefa})