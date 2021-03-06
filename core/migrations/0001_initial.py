# Generated by Django 2.1.2 on 2018-10-31 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriaproduto',
            fields=[
                ('pkid_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nomecategoria', models.CharField(max_length=100, unique=True, verbose_name='Nome da Categoria')),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias (Produto)',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cotacaocompra',
            fields=[
                ('pkid_cotacao', models.AutoField(primary_key=True, serialize=False)),
                ('fornecedor', models.CharField(blank=True, max_length=100, null=True)),
                ('dt_cotacao', models.DateTimeField(blank=True, null=True)),
                ('dt_entrega', models.DateTimeField(blank=True, null=True)),
                ('formapamento', models.CharField(blank=True, max_length=45, null=True)),
                ('pedidocompra_pkid_compra', models.IntegerField()),
                ('statuscotacao_pkid_status', models.IntegerField()),
                ('dt_cadastro', models.DateTimeField(blank=True, null=True)),
                ('dt_alteracao', models.DateTimeField(blank=True, null=True)),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('pkid_endereco', models.AutoField(primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=100, verbose_name='Endereço')),
                ('endereco_numero', models.CharField(blank=True, max_length=7, null=True, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=45, null=True, verbose_name='Complemento')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='Estado')),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Endereço (Pessoa : CEP)',
                'verbose_name_plural': 'Endereços',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('pkid_entrega', models.AutoField(primary_key=True, serialize=False)),
                ('dataentrega', models.DateTimeField(blank=True, null=True)),
                ('valorfrete', models.TextField(blank=True, null=True)),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Forma de Entrega',
                'verbose_name_plural': 'Formas de Entrega',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Formapagamento',
            fields=[
                ('pkid_formapag', models.AutoField(primary_key=True, serialize=False)),
                ('formapagamento', models.CharField(max_length=50)),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Forma de Pagamento',
                'verbose_name_plural': 'Formas de Pagamento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Formulamateria',
            fields=[
                ('pkid_formula_materia', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.FloatField(verbose_name='Quantidade')),
            ],
            options={
                'verbose_name': 'Matéria Prima : Fórmula',
                'verbose_name_plural': 'Matérias Fórmulas (Relação)',
            },
        ),
        migrations.CreateModel(
            name='Formulaproduto',
            fields=[
                ('pkid_formula', models.AutoField(primary_key=True, serialize=False)),
                ('tempomaturacao', models.TimeField(verbose_name='Tempo de Maturação')),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Fórmula Produto',
                'verbose_name_plural': 'Fórmulas (Produto)',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Itemcompra',
            fields=[
                ('pkid_item', models.AutoField(primary_key=True, serialize=False)),
                ('produto', models.CharField(blank=True, max_length=45, null=True)),
                ('descricaoproduto', models.CharField(blank=True, max_length=45, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('precounitario', models.TextField(blank=True, null=True)),
                ('totalvenda', models.TextField(blank=True, null=True)),
                ('dt_cadastro', models.DateTimeField(blank=True, null=True)),
                ('dt_alteracao', models.DateTimeField(blank=True, null=True)),
                ('hide', models.BooleanField(default=0)),
                ('pedidocompra_pkid_compra', models.IntegerField()),
                ('statuscompra_pkid_status', models.IntegerField()),
                ('unidademedidacompra_pkid_unidademedida', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Itemcotacao',
            fields=[
                ('pkid_item', models.AutoField(primary_key=True, serialize=False)),
                ('produto', models.CharField(blank=True, max_length=45, null=True)),
                ('descricaoproduto', models.CharField(blank=True, max_length=100, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('precounitario', models.TextField(blank=True, null=True)),
                ('totalvenda', models.TextField(blank=True, null=True)),
                ('dt_cadastro', models.DateTimeField(blank=True, null=True)),
                ('dt_alteracao', models.DateTimeField(blank=True, null=True)),
                ('hide', models.BooleanField(default=0)),
                ('cotacaocompra_pkid_cotacao', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Itemvenda',
            fields=[
                ('pkid_itemvenda', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
                ('vl_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vl_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Materiaprima',
            fields=[
                ('pkid_materiaprima', models.AutoField(primary_key=True, serialize=False)),
                ('materiaprima', models.CharField(max_length=60, verbose_name='Matéria Prima')),
                ('marca', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca')),
                ('totalestoque', models.IntegerField(verbose_name='Qtd. em Estoque')),
                ('hide', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Matéria Prima',
                'verbose_name_plural': 'Matérias Primas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('pkid_movimentacao', models.AutoField(primary_key=True, serialize=False)),
                ('fkid_produto', models.IntegerField()),
                ('tipomovimentacao', models.TextField()),
                ('numentradas', models.IntegerField()),
                ('numsaidas', models.IntegerField()),
                ('dt_cadastro', models.DateTimeField()),
                ('dt_alteracao', models.DateTimeField()),
                ('hide', models.BooleanField(default=0)),
                ('fkid_linhavenda1', models.IntegerField(blank=True, null=True)),
                ('fkid_venda', models.IntegerField(blank=True, null=True)),
                ('fkid_pedidofabri', models.IntegerField(blank=True, null=True)),
                ('fkid_estoque', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pedidocompra',
            fields=[
                ('pkid_compra', models.AutoField(primary_key=True, serialize=False)),
                ('fornecedor', models.CharField(blank=True, max_length=100, null=True)),
                ('dt_pedido', models.DateTimeField(blank=True, null=True)),
                ('dt_compra', models.DateTimeField(blank=True, null=True)),
                ('dt_pagamento', models.DateTimeField(blank=True, null=True)),
                ('dt_recebimento', models.DateTimeField(blank=True, null=True)),
                ('cotacaocompra_pkid_cotacao', models.IntegerField()),
                ('dt_cadastro', models.DateTimeField(blank=True, null=True)),
                ('dt_alteracao', models.DateTimeField(blank=True, null=True)),
                ('hide', models.BooleanField(default=0)),
                ('statuscompra_pkid_status', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pedidofabricacao',
            fields=[
                ('pkid_pedidofabricacao', models.AutoField(primary_key=True, serialize=False)),
                ('lote', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('dt_fim_maturacao', models.DateTimeField()),
                ('hide', models.BooleanField(default=0)),
                ('fkid_formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Formulaproduto')),
            ],
            options={
                'verbose_name': 'Pedido de Fabricação',
                'verbose_name_plural': 'Pedidos de Fabricação',
            },
        ),
        migrations.CreateModel(
            name='Pedidovenda',
            fields=[
                ('pkid_venda', models.AutoField(primary_key=True, serialize=False)),
                ('dt_pedido', models.DateTimeField(blank=True, null=True)),
                ('dt_pagamento', models.DateTimeField(blank=True, null=True)),
                ('dt_preventrega', models.DateTimeField(blank=True, null=True)),
                ('pago', models.BooleanField(default=0)),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Pedido de Venda',
                'verbose_name_plural': 'Pedidos de Venda',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('pkid_pessoa', models.AutoField(primary_key=True, serialize=False)),
                ('nomecompleto_razaosocial', models.CharField(max_length=100, verbose_name='Nome / Razão Social')),
                ('apelido_nomefantasia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apelido / Nome Fantasia')),
                ('email', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='E-mail')),
                ('cpf_cnpj', models.CharField(blank=True, max_length=19, null=True, unique=True, verbose_name='CPF / CNPJ')),
                ('rg_ie', models.CharField(blank=True, max_length=50, null=True, verbose_name='RG / IE')),
                ('genero', models.CharField(max_length=1, verbose_name='Gênero')),
                ('dt_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('st_pessoajuridica', models.BooleanField(default=0, max_length=1, verbose_name='Pessoa Jurídica')),
                ('tipopessoa', models.CharField(max_length=15, verbose_name='Tipo da Pessoa')),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('pkid_produto', models.AutoField(primary_key=True, serialize=False)),
                ('codproduto', models.CharField(max_length=8, unique=True, verbose_name='Código')),
                ('nomeproduto', models.CharField(max_length=50, verbose_name='Nome do Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('precocusto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço de Custo')),
                ('totalestoque', models.IntegerField(default=0, verbose_name='Qtd. em Estoque')),
                ('descricao', models.CharField(blank=True, max_length=300, null=True, verbose_name='Descrição')),
                ('sabor', models.CharField(blank=True, max_length=45, null=True, verbose_name='Sabor')),
                ('marca', models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca')),
                ('altura', models.IntegerField(verbose_name='Altura')),
                ('largura', models.IntegerField(verbose_name='Largura')),
                ('profundidade', models.IntegerField(verbose_name='Profundidade')),
                ('peso', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Peso')),
                ('fotoproduto', models.FileField(blank=True, max_length=1000, null=True, upload_to='uploads/%Y/%m', verbose_name='Foto do Produto')),
                ('vendivel', models.BooleanField(default=1)),
                ('hide', models.BooleanField(default=0)),
                ('fkid_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Categoriaproduto', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Statuscompra',
            fields=[
                ('pkid_status', models.AutoField(primary_key=True, serialize=False)),
                ('descricaostatus', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Statusfabricacao',
            fields=[
                ('pkid_status', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.IntegerField(verbose_name='Ordem')),
                ('status', models.CharField(blank=True, max_length=45, null=True, verbose_name='Estado')),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Status de Fabricação',
                'verbose_name_plural': 'Status de Fabricação',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Statusvenda',
            fields=[
                ('pkid_status', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Status de Venda',
                'verbose_name_plural': 'Status de Venda',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('pkid_telefone', models.AutoField(primary_key=True, serialize=False)),
                ('ddi', models.CharField(blank=True, default=55, max_length=3, null=True, verbose_name='DDI')),
                ('ddd', models.CharField(blank=True, default=11, max_length=2, null=True, verbose_name='DDD')),
                ('numero', models.CharField(max_length=15, verbose_name='Número')),
                ('hide', models.BooleanField(default=0)),
                ('fkid_pessoa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoEntrega',
            fields=[
                ('pkid_tipoentrega', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=30, verbose_name='TipoEntrega')),
            ],
        ),
        migrations.CreateModel(
            name='Unidademedida',
            fields=[
                ('pkid_unidademedida', models.AutoField(primary_key=True, serialize=False)),
                ('unidademedida', models.CharField(max_length=50, verbose_name='Unidade')),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Unidade de Medida',
                'verbose_name_plural': 'Unidades de Medida',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('pkid_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nomecompleto', models.CharField(max_length=45)),
                ('login', models.CharField(max_length=45, unique=True)),
                ('senha', models.CharField(max_length=45)),
                ('dt_importacao', models.DateTimeField()),
                ('dt_alteracao', models.DateTimeField()),
                ('hide', models.BooleanField(default=0)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuarioalteracao',
            fields=[
                ('pkid_usuario_alteracao', models.AutoField(primary_key=True, serialize=False)),
                ('dt_alteracao', models.DateTimeField()),
                ('tipo_alteracao', models.TextField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='produto',
            name='fkid_unidademedida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Unidademedida', verbose_name='Unidade de Medida'),
        ),
        migrations.AddField(
            model_name='pedidovenda',
            name='fkid_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa'),
        ),
        migrations.AddField(
            model_name='pedidovenda',
            name='fkid_formapag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Formapagamento'),
        ),
        migrations.AddField(
            model_name='pedidovenda',
            name='fkid_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Statusvenda'),
        ),
        migrations.AddField(
            model_name='pedidovenda',
            name='fkid_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pedidofabricacao',
            name='fkid_statusfabricacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Statusfabricacao'),
        ),
        migrations.AddField(
            model_name='materiaprima',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Unidademedida', verbose_name='Unidade'),
        ),
        migrations.AddField(
            model_name='itemvenda',
            name='fkid_pedidovenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pedidovenda'),
        ),
        migrations.AddField(
            model_name='itemvenda',
            name='fkid_produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Produto'),
        ),
        migrations.AlterUniqueTogether(
            name='itemcotacao',
            unique_together={('pkid_item', 'cotacaocompra_pkid_cotacao')},
        ),
        migrations.AlterUniqueTogether(
            name='itemcompra',
            unique_together={('pkid_item', 'pedidocompra_pkid_compra')},
        ),
        migrations.AddField(
            model_name='formulaproduto',
            name='fkid_produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Produto', verbose_name='Produto'),
        ),
        migrations.AddField(
            model_name='formulamateria',
            name='fkid_formulaproduto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Formulaproduto', verbose_name='Fórmula'),
        ),
        migrations.AddField(
            model_name='formulamateria',
            name='fkid_materiaprima',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Materiaprima', verbose_name='Matéria Prima'),
        ),
        migrations.AddField(
            model_name='formulamateria',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Unidademedida', verbose_name='Unidade'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='fkid_tipoentrega',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoEntrega'),
        ),
        migrations.AddField(
            model_name='entrega',
            name='fkid_venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pedidovenda'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='fkid_pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa', verbose_name='Pessoa'),
        ),
        migrations.AlterUniqueTogether(
            name='itemvenda',
            unique_together={('pkid_itemvenda', 'fkid_pedidovenda')},
        ),
    ]
