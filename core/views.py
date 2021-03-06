"""
    Contém as views principais do sistema
    as views especificas estão na pasta my_views e custom
    Também é utilizado os arquivos funcoes.py
"""

from django.shortcuts import render, redirect

import core.forms as forms
import core.models as model

from core.funcoes import *
from core.my_views.clientes import *
from core.my_views.produtos import *
from core.my_views.usuario import *
from core.my_views.producao import *
from core.my_views.fornecedores import *
from core.api.api import *

# Create your views here.


def index(request):
    """ Retorna a página inicial (Login) """

    return render(request, "index.html")

# Home e Principais


@login_required(login_url="/admin")
def home(request):
    """ Página Principal do sistema
        Segura o iframe
    """
    
    statusVendas = [
        stat.descricao for stat in models.Statusvenda.objects
        .all()
        .order_by('order')
    ]
    print(statusVendas)

    context = {
        "statusVendas":statusVendas,
    }

    return render(request, "base.html", context)


@login_required(login_url="/admin")
def redirect_home(request):
    """ Redirect para a Página Inicial """
    return redirect('/admin/home')


@login_required(login_url="/admin")
def iframe_home(request):
    """ Página inicial no iframe """

    # Info sobre pedidos de fabricação
    pedidosFabricacao = models.Pedidofabricacao.objects.filter(
        hide=False
    ).exclude(
        fkid_statusfabricacao__order=3
    ).order_by(
        '-fkid_statusfabricacao', 'dt_fim_maturacao'
    )

    context = {
        "fabricacaoPiece":"iframe/pieces/fabricacaoDetail.html",
        "pedidosFabricacao":pedidosFabricacao
    }
    return render(request, "iframe/home.html", context)

# Frete


@login_required(login_url="/admin")
def calcula_frete(request):
    """ Sem uso no momento """

    retorno = {"Valor": "0,00", "PrazoEntrega": 0, "MsgErro": "None"}
    if request.POST:
        form = forms.FreteForm(request.POST)
        if form.is_valid():
            # Arruma os campos de altura, comprimento e largura para não dar erro.
            if form.cleaned_data['nVlAltura'] < 2:
                form.cleaned_data['nVlAltura'] = 2
            if form.cleaned_data['nVlComprimento'] < 16:
                form.cleaned_data['nVlComprimento'] = 16
            if form.cleaned_data['nVlLargura'] < 11:
                form.cleaned_data['nVlLargura'] = 11

            try:
                retorno = calcula_frete(
                    form.cleaned_data['nCdServico'],
                    form.cleaned_data['sCepOrigem'],
                    form.cleaned_data['sCepDestino'],
                    form.cleaned_data['nVlPeso'],
                    form.cleaned_data['nCdFormato'],
                    form.cleaned_data['nVlComprimento'],
                    form.cleaned_data['nVlAltura'],
                    form.cleaned_data['nVlLargura']
                )
            except:
                print("Você está sem internet")
    else:
        form = forms.FreteForm()
    context = {
        "form": form,
        "Valor": retorno.get('Valor'),
        "PrazoEntrega": retorno.get('PrazoEntrega'),
        "MsgErro": retorno.get('MsgErro')
    }
    return render(request, "iframe/vendas/calcula_frete.html", context)
