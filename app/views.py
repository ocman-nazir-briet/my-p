from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


def index(request):
    authors = Author.objects.all()
    authorsCount = Author.objects.all().count()
    
    obj = Testt.objects.filter(name__startswith='tt')
    # print(obj)
    # print(authorsCount)
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
            messages.error(request, 'Something Went Wrong, Form not Submitted')
    return render(request, 'index.html', {'authors':authors, 'authorsCount':authorsCount,'form':form, 'form1':form1, 'form2':form2})

def blog(request):
    if request.method =='POST':
        form = blogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Something Went Wrong, Form not Submitted')

    return redirect('/')

def school(request):
    if request.method =='POST':
        form = schoolForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Something Went Wrong, Form not Submitted')

    return redirect('/')

def tes(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        des = request.POST.get('des')
        Testt.objects.create(name = name, des = des)
        return redirect('/')

