from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, AutorForm, CategoriaForm, BuscaForm

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('criar_post')
    else:
        form = PostForm()
    return render(request, 'criar_post.html', {'form': form})

def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()
    return render(request, 'criar_autor.html', {'form': form})

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()
    return render(request, 'criar_categoria.html', {'form': form})

def buscar_post(request):
    resultados = []
    if request.method == 'POST':
        form = BuscaForm(request.POST)
        if form.is_valid():
            termo = form.cleaned_data['termo']
            resultados = Post.objects.filter(titulo__icontains=termo)
    else:
        form = BuscaForm()
    return render(request, 'buscar.html', {'form': form, 'resultados': resultados})
