from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'marca', 'categoria']


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']


def cadastrar_marca(request, template_name='marca/marca_form.html'):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_marca')
    return render(request, template_name, {'form': form})


def listar_marca(request, template_name="marca/marca_list.html"):
    query = request.GET.get("busca")
    if query:
        marca = Marca.objects.filter(nome__icontains=query)
    else:
        marca = Marca.objects.all()
    marcas = {'lista': marca}
    return render(request, template_name, marcas)


def editar_marca(request, pk, template_name='marca/marca_form.html'):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marca')
    else:
        form = MarcaForm(instance=marca)
    return render(request, template_name, {'form': form})


def remover_marca(request, pk, template_name='marca/marca_delete.html'):
    marca = Marca.objects.get(pk = pk)
    if request.method == "POST":
        marca.delete()
        return redirect('listar_marca')
    return render(request, template_name, {'marca': marca})


def listar_produtos_marca(request, pk, template_name="marca/marca_produtos_list.html"):
    produtos = Produto.objects.filter(marca = pk)
    return render(request, template_name, {'produtos': produtos})


def cadastrar_produto(request, template_name='produto/produto_form.html'):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_produto')
    return render(request, template_name, {'form': form})


def listar_produto(request, template_name="produto/produto_list.html"):
    query = request.GET.get("busca")
    if query:
        produto = Produto.objects.filter(descricao__icontains=query)
    else:
        produto = Produto.objects.all()
    produtos = {'lista': produto}
    return render(request, template_name, produtos)


def perfil_produto(request, pk, template_name="produto/produto_show.html"):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, template_name, {'produto': produto})


def editar_produto(request, pk, template_name='produto/produto_form.html'):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produto')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, template_name, {'form': form})


def remover_produto(request, pk, template_name='produto/produto_delete.html'):
    produto = Produto.objects.get(pk = pk)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produto')
    return render(request, template_name, {'produto': produto})


def cadastrar_categoria(request, template_name='categoria/categoria_form.html'):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_categoria')
    return render(request, template_name, {'form': form})

def listar_categoria(request, template_name="categoria/categoria_list.html"):
    query = request.GET.get("busca")
    if query:
        categoria = Categoria.objects.filter(descricao__icontains=query)
    else:
        categoria = Categoria.objects.all()
    categoria = {'lista': categoria}
    return render(request, template_name, categoria)


def editar_categoria(request, pk, template_name='categoria/categoria_form.html'):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, template_name, {'form': form})


def remover_categoria(request, pk, template_name='categoria/categoria_delete.html'):
    categoria = Categoria.objects.get(pk = pk)
    if request.method == "POST":
        categoria.delete()
        return redirect('listar_produto')
    return render(request, template_name, {'categoria': categoria})


def listar_produtos_categoria(request, pk, template_name="categoria/categoria_produtos_list.html"):
    produtos = Produto.objects.filter(categoria = pk)
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, template_name, {'produtos': produtos, 'categoria': categoria})