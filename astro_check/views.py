from django.contrib.auth.decorators import login_required

from astro_check.forms import AstroCheck
from astro_check.utils import get_role, get_team
from loginsys.views import *
from django.shortcuts import render


def main(request):
    return render(request, 'astro_check/main.html')


@login_required
def astro_check(request):
    context = {
        'title': 'Проверка на совместимость',
    }
    if request.method == 'POST':
        form = AstroCheck(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            patronymic = form.cleaned_data['patronymic']
            role = get_role(form.cleaned_data['role'])
            email = form.cleaned_data['email']
            team = get_team(form.cleaned_data['team'])
            date = int(form.cleaned_data['date'])
            month = form.cleaned_data['month']
            year = int(form.cleaned_data['year'])
            hours = int(form.cleaned_data['hours'])
            minutes = int(form.cleaned_data['minutes'])
            time_zone = form.cleaned_data['time_zone']
            city = form.cleaned_data['city']

            print(name, surname, patronymic, role, email, team, date, month, year, hours, minutes, time_zone, city)

            context = {
                'title': f'Совместимость кандидата {surname} {name}',
            }
            return render(request, 'astro_check/astro_result_page.html', context)
        else:
            context.update({'form': form})
    else:
        form = AstroCheck(request.POST)
        context.update({'form': form})

    return render(request, 'astro_check/astro_check_page.html', context=context)
