from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Produto, Tag, Categoria


def Index(request):

    produto = Produto.objects.all().order_by()[:8]
    cate = Produto.objects.all().order_by('-id')[:4]

    contexto = {
        'produtos': produto,
        'categorias': cate
    }

    return render(request, 'app_pharma/index.html', {'contexto': contexto})


def Detalhe(request, id):
    produto = Produto.objects.filter(id=id)
    
    return render(request, 'app_pharma/detalhes.html', {'produtos': produto})


def Busca(request, *args, **kwargs):
    buscar = request.GET.get('busca')
    
      
    if buscar.strip() == '':
        return render(request, 'app_pharma/busca.html')
    
    produto = Produto.objects.filter(nome_produto__icontains=buscar)
    tag = Tag.objects.filter(tag__icontains=buscar).values()
    categoria = Categoria.objects.filter(categoria__icontains=buscar).values()
    
    if(tag):
        produto = Produto.objects.filter(tag_id=tag[0]['id'])
        
    elif(categoria):
        produto=Produto.objects.filter(categoria__id=categoria[0]['id'])
        
        
    
    contexto = {
        'produtos': produto,
        'busca': buscar
    }
    return render(request, 'app_pharma/busca.html', {'contexto': contexto})
    
    
     
    
  
