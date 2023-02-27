from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    authors = Author.objects.all()
    form = authorForm()
    if request.method == 'POST':
        form = authorForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'authors':authors, 'form':form})