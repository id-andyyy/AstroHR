from django.contrib.auth.decorators import login_required

from loginsys.views import *
from django.shortcuts import render


def main(request):
    return render(request, 'astro_check/main.html')


def astro_check(request):
    context = {
        'title': 'Проверка на совместимость',
    }
    return render(request, 'astro_check/astro_check_page.html', context=context)
