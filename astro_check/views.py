from django.contrib.auth.decorators import login_required

from loginsys.views import *
from django.shortcuts import render


def astro_check(request):
    if request.user.is_authenticated:
        hr_name = request.user.first_name
    else:
        hr_name = 'не вошли в систему'
    context = {
        'title': 'Проверка на совместимость',
        'hr_name': hr_name,
    }
    return render(request, 'astro_check/astro_check_page.html', context=context)
