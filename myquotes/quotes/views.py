# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, AuthorForm, QuoteForm
from .models import Quote, Author, Tag
from django.db.models import Count

"""def author_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'quotes/author_detail.html', {'author': author})"""

def top_tags(request):
    return {'top_tags': Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]}

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    quotes = author.quotes.all()
    return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})

def tag_detail(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = tag.quote_set.all()
    return render(request, 'quotes/tag_detail.html', {'tag': tag, 'quotes': quotes})

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('quotes:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:all_quotes')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:all_quotes')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

def all_quotes(request, tag_slug=None):
    if tag_slug:
        tag = Tag.objects.get(slug=tag_slug)
        quotes = Quote.objects.filter(tags=tag)
    else:
        quotes = Quote.objects.all()

    paginator = Paginator(quotes, 10)  # Show 10 quotes per page
    page = request.GET.get('page')

    try:
        quotes = paginator.page(page)
    except PageNotAnInteger:
        quotes = paginator.page(1)
    except EmptyPage:
        quotes = paginator.page(paginator.num_pages)

    return render(request, 'quotes/all_quotes.html', {'page': page, 'quotes': quotes})

def top_tags(request):
    tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]
    return {'top_tags': tags}

