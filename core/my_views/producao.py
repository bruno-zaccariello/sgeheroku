"""
    Módulo que contem as views de produção
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.forms import inlineformset_factory
from django.urls import reverse

from core.funcoes import arruma_url_page
from core.models import *
from core.forms import *


@login_required(login_url="/admin")
def lista_formula(request):
    """ Página com a lista de fórmulas """

    formulas = Formulaproduto.objects.filter(hide=False)
    page = int(request.GET.get('page', 1))
    deletado = request.GET.get('deleted', False)

    paginas = Paginator(formulas, 10)
    pagina = paginas.get_page(page)

    url = arruma_url_page(request)
    context = {
        "pagina": pagina,
        "success": deletado,
        "url": url,
    }
    return render(request, 'iframe/producao/formula/lista_formulas.html', context)


@login_required(login_url="/admin")
def pagina_formula(request, id_formula):
    """ Página individual da fórmula """

    try:
        formula = Formulaproduto.objects.filter(
            hide=False).get(pkid_formula=id_formula)
    except:
        formula = None

    success = request.GET.get('success', False)

    formset_materias = inlineformset_factory(
        Formulaproduto,
        Formulamateria,
        extra=0,
        min_num=1,
        exclude=[],
        form=FormulamateriaForm)

    if request.POST:
        with transaction.atomic():
            form_formula = FormulaCompletaForm(request.POST, instance=formula)

            if form_formula.is_valid():
                saved_formula = form_formula.save(commit=False)
                saved_formula.save()

                forms_materia = formset_materias(
                    request.POST, instance=saved_formula)

                if forms_materia.is_valid():
                    forms_materia.save()

                url = str(request.path_info) + str('?success=True')
                return HttpResponseRedirect(url)
    else:
        form_formula = FormulaCompletaForm(instance=formula)
        forms_materia = formset_materias(instance=formula)

    context = {
        "Formula": formula,
        "form_formula": form_formula,
        "forms_materia": forms_materia,
        "success": success
    }
    return render(request, "iframe/producao/formula/pagina_formula.html", context)


@login_required(login_url="/admin")
def deletar_formula(request, id_formula):
    """ API para deletar uma fórmula """

    formula = Formulaproduto.objects.get(pkid_formula=id_formula)
    formula.hide = True
    formula.save()
    return HttpResponseRedirect('/iframe/producao/formulas/lista/?deleted=True')


@login_required(login_url="/admin")
def nova_fabricacao(request):
    """ Página para criar um novo pedido de fabricação """

    id_fabricacao = 0
    success = request.GET.get('success', False)
    if request.POST:
        form_fabricacao = PedidofabricacaoForm(request.POST)
        if form_fabricacao.is_valid():
            # Salva em falso para pegar o id
            form_fabricacao = form_fabricacao.save(commit=False)
            form_fabricacao.save()
            id_fabricacao = form_fabricacao.pk
            print(id_fabricacao)
            # Com o id pego atualiza o estoque das matérias-primas
            Pedidofabricacao.objects.get(pkid_pedidofabricacao=id_fabricacao).remover_estoque()
            url = str(request.path_info) + '?success=True'
            return HttpResponseRedirect(url)
    else:
        form_fabricacao = PedidofabricacaoForm()
    context = {
        "fabricaForm": PedidofabricacaoForm,
        "success": success,
        "id_fabricacao":id_fabricacao
    }
    return render(request, "iframe/producao/pedidos/nova_fabricacao.html", context)


@login_required(login_url="/admin")
def editar_fabricacao(request, id_fabricacao):
    """ Pagina para editar um pedido de fabricação """

    success = request.GET.get('success', False)
    try:
        fabricacao = Pedidofabricacao.objects.get(
            pkid_pedidofabricacao=id_fabricacao)
    except:
        return HttpResponseRedirect(reverse('lista_fabricacao'))

    if request.POST:
        form_fabricacao = PedidofabricacaoForm(
            request.POST, instance=fabricacao)
        if form_fabricacao.is_valid():
            form_fabricacao.save()
            url = str(request.path_info) + '?success=True'
            return HttpResponseRedirect(url)
    else:
        form_fabricacao = PedidofabricacaoForm(instance=fabricacao)
    context = {
        "fabricaForm": form_fabricacao,
        "pedidoFabricacao": fabricacao,
        "id_fabricacao":id_fabricacao,
        "success": success,
    }
    return render(request, "iframe/producao/pedidos/editar_fabricacao.html", context)


@login_required(login_url="/admin")
def lista_fabricacao(request):
    """ Página que exibe a lista de pedidos de fabricação """

    # Pega informações da URL
    deletado = request.GET.get('deleted', False)
    page = int(request.GET.get('page', 1))
    update = int(request.GET.get('update', False))
    print(update)
    if update:
        Pedidofabricacao.objects.get(pkid_pedidofabricacao=update).avancar_etapa()
        return HttpResponseRedirect(request.path_info)

    # Filtra lista de pedidos e gera páginas
    pedidos = Pedidofabricacao.objects.filter(hide=False)
    paginas = Paginator(pedidos, 10)
    pagina = paginas.get_page(page)
    url = arruma_url_page(request)  # função em funcoes.py

    context = {
        'pagina': pagina,
        'deletado': deletado
    }

    return render(request, "iframe/producao/pedidos/lista_fabricacao.html", context)

@login_required(login_url="/admin")
def deletar_fabricacao(request, id_fabricacao):
    """ API Para deletar um pedido de fabricação"""
    try:
        Pedidofabricacao.objects.get(pkid_pedidofabricacao=id_fabricacao).voltar_estoque().delete()
        url = reverse('lista_fabricacao') + '?deleted=True'
        return HttpResponseRedirect(url)
    except:
        return HttpResponseRedirect(reverse('lista_fabricacao'))
