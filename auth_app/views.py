from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from auth_app.forms import CustomUserCreationForm, CustomUserLogin


def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = CustomUserCreationForm()
    tickers = range(1, 10)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    context = {
        'form': form,
        'tickers': tickers,
    }
    return render(request, 'auth_app/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = CustomUserLogin()
    context = {'form': form}
    tickers = range(1, 10)
    context['tickers'] = tickers
    if request.method == "POST":
        form = CustomUserLogin(request.POST)
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        context['form'] = form
        context['error'] = 'Невірне імʼя або пароль'

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'auth_app/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('index')
