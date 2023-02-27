from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


def index(request):
    authors = Author.objects.all()
    authorsCount = Author.objects.all().count()
    print(authorsCount)
    form = authorForm()
    form1 = blogForm()
    form2 = schoolForm()
    if request.method == 'POST':
        form = authorForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Something Went Wrong')
    return render(request, 'index.html', {'authors':authors, 'form':form, 'form1':form1, 'form2':form2})

def blog(request):
    if request.method =='POST':
        form = blogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Something Went Wrong')

    return redirect('/')

def school(request):
    if request.method =='POST':
        form = schoolForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Something Went Wrong')

    return redirect('/')

def tes(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Testt.objects.create(name = name)
        return redirect('/')

