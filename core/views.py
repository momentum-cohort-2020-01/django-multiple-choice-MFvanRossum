from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from .models import Snippet, Tag
from .forms import SnippetForm
from users.models import User

@login_required
def profile(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/profile.html', {'snippets': snippets})

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
