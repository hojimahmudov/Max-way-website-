from django.shortcuts import render, redirect
from product.models import Category, Product
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import login as dj_login, authenticate


# Create your views here.

def index(request):
    categorys = Category.objects.prefetch_related('product_set').all()

    context = {
        "categorys": categorys,

    }
    return render(request, 'index.html', context)


def order(request):
    return render(request, "order.html", {})


def register(request):
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, "register.html", context)


def login(request):
    form = LoginForm()
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(username=username, phone_number=phone_number, password=password)
            if user is not None:
                dj_login(request, user)
                return redirect('order')

    context = {
        'form': form
    }

    return render(request, "login.html", context)
