from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Modalidade, Nivel


def index(request):
    todas_modalidades_list = Modalidade.objects.order_by('modalidade_pub_date')[:]
    context = {'todas_modalidades_list': todas_modalidades_list}
    return render(request, 'fichas/index.html', context)


# def modalidade(request, modalidade_id):
#     return HttpResponse(f"Aqui vamos detalhar a modalidade {modalidade_id}")

def modalidade(request, modalidade_id):
    mod_chose = Modalidade.objects.get(id=modalidade_id)

    todos_os_niveis = Nivel.objects.order_by('id')[:]

    context = {'todos_os_niveis': todos_os_niveis, 'modalidade_id': modalidade_id, 'mod_chose': mod_chose.modalidade_nome}
    return render(request, 'fichas/niveis.html', context)
