from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from .forms import UserLoginForm


def user_login(request):
    context = {'title': 'Вход'}
    context.update(csrf(request))
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('astro_check')
        else:
            form = UserLoginForm()
            messages.error(request, 'Пользователь не найден')
    else:
        form = UserLoginForm()
    context.update({'form': form})
    return render(request, 'loginsys/login_page.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')
