from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from .models import Snippet, Tag
from .forms import SnippetForm
from users.models import User
from django.db.models import Q

@login_required
def profile(request):
    def create_db_query(query_string):
        query_terms = query_string.split(" ")
        db_query = Q()
        for term in query_terms:
            db_query = db_query | Q(title__icontains=term) | Q(language__icontains=term) | Q(code__icontains=term) | Q(description__icontains=term)
        return db_query
    query = request.GET.get('q')
    if query:
        snippets = Snippet.objects.filter(create_db_query(query), users=request.user)
    else:
        snippets = Snippet.objects.filter(users=request.user)
    context = {'snippets': snippets}
    context['query'] = str(query)
    return render(request, 'core/profile.html', context=context)

def new_snippet(request):
    snippets = Snippet.objects.all()
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save()
            snippet.users.add(request.user)
            return redirect('profile')
    else:
            form = SnippetForm()
    return render(request, 'core/new_snippet.html', {'form': form, 'snippets': snippets})

def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save()
            return redirect('profile')
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'core/edit_snippet.html', {'snippet': snippet, 'form':form, 'pk': pk})

def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return redirect ('profile')

def library(request):
    def library_query(query_string):
        query_terms = query_string.split(" ")
        db_query = Q()
        for term in query_terms:
            db_query = db_query | Q(title__icontains=term) | Q(language__icontains=term) | Q(code__icontains=term) | Q(description__icontains=term)
        return db_query
    query = request.GET.get('lib-search')
    if query:
        snippets = Snippet.objects.filter(library_query(query))
    else: 
        snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    context['query'] = str(query)
    return render(request, 'core/library.html', context=context)

# def library(request):
#     snippets = Snippet.objects.all()
#     return render(request, 'core/library.html', {'snippets': snippets})