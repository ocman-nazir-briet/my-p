from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    authors = Author.objects.all()
    form = authorForm()
    form1 = blogForm()
    if request.method == 'POST':
        form = authorForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'authors':authors, 'form':form, 'form1':form1})

def blog(request):
    if request.method =='POST':
        form1 = blogForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            form1.errors()

    return redirect('/')