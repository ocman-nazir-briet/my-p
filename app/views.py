from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


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
        else:
            messages.error(request, 'Something Went Wrong')
    return render(request, 'index.html', {'authors':authors, 'form':form, 'form1':form1})

def blog(request):
    if request.method =='POST':
        form1 = blogForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            messages.error(request, 'Something Went Wrong')

    return redirect('/')