from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden # Импорт для запрета доступа
from django.db.models import Q
from .models import Article
from .forms import ArticleForm

# 1. Список статей + Поиск
def article_list(request):
    search_query = request.GET.get('q', '')
    
    if search_query:
        # Поиск по заголовку ИЛИ автору.
        articles = Article.objects.filter(
            Q(title__icontains=search_query) | 
            Q(author__username__icontains=search_query) | # Исправил поиск по автору (т.к. теперь это User)
            Q(pub_date__icontains=search_query)
        )
    else:
        articles = Article.objects.all().order_by('-pub_date')

    return render(request, 'blog/article_list.html', {'articles': articles})

# НОВАЯ ФУНКЦИЯ: Только мои статьи
@login_required
def my_articles(request):
    # Фильтруем: автор равен текущему пользователю
    articles = Article.objects.filter(author=request.user).order_by('-pub_date')
    # Используем тот же шаблон, но передаем флаг is_my_articles (для заголовка, если захочешь)
    return render(request, 'blog/article_list.html', {'articles': articles})

# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# 2. Добавление статьи
@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Новая статья'})

# 3. Редактирование (с ЗАЩИТОЙ)
@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    # Проверка: если ты не автор - иди лесом
    if request.user != article.author:
        return HttpResponseForbidden("У вас нет прав на редактирование этой статьи.")

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Редактирование'})

# 4. Удаление (с ЗАЩИТОЙ)
@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # Проверка: если ты не автор - удалять нельзя
    if request.user != article.author:
        return HttpResponseForbidden("У вас нет прав на удаление этой статьи.")

    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})