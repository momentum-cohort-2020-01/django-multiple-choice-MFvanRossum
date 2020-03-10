from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from .models import Snippet, Tag
from users.models import User
# from .forms import ...

@login_required
def profile(request):
    snippets = Snippet.objects.all()
    return render(request, 'core/profile.html', {'snippets': snippets})
