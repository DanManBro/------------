from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Article
from .forms import ArticleForm

# 1. Список статей + Поиск
def article_list(request):
    search_query = request.GET.get('q', '')
    
    if search_query:
        # Поиск по заголовку ИЛИ автору. 
        # (По дате тоже ищет, если ввести формат ГГГГ-ММ-ДД)
        articles = Article.objects.filter(
            Q(title__icontains=search_query) | 
            Q(author__icontains=search_query) |
            Q(pub_date__icontains=search_query)
        )
    else:
        articles = Article.objects.all().order_by('-pub_date')

    return render(request, 'blog/article_list.html', {'articles': articles})

# 2. Добавление статьи
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Новая статья'})

# 3. Редактирование
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Редактирование'})

# 4. Удаление
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})