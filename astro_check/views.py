from django.contrib.auth.decorators import login_required

from astro_check.forms import AstroCheck
from astro_check.utils import get_role, get_team, get_asc_num, get_team_compatibility, get_company_compatibility, \
    get_team_message, get_company_message
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
            day = int(form.cleaned_data['day'])
            month = int(form.cleaned_data['month'])
            year = int(form.cleaned_data['year'])
            hours = int(form.cleaned_data['hours'])
            minutes = int(form.cleaned_data['minutes'])
            time_zone = int(form.cleaned_data['time_zone'])
            city = form.cleaned_data['city']

            ascendant = get_asc_num(day, month, year, city, hours, minutes, time_zone)

            team_compatibility = get_team_compatibility(form.cleaned_data['team'], ascendant)
            company_compatibility = get_company_compatibility(ascendant)

            team_message = get_team_message(ascendant, team_compatibility)
            company_message = get_company_message(ascendant, company_compatibility)

            context = {
                'title': f'Совместимость кандидата {surname} {name}',
                'name': name,
                'surname': surname,
                'patronymic': patronymic,
                'day': day,
                'month': month,
                'year': year,
                'email': email,
                'role': form.cleaned_data['role'],
                'team': form.cleaned_data['team'],
                'ascendant': ascendant,
                'team_compatibility': team_compatibility,
                'team_message': team_message,
                'company_compatibility': company_compatibility,
                'company_message': company_message,
            }
            return render(request, 'astro_check/astro_result_page.html', context)
        else:
            context.update({'form': form})
    else:
        form = AstroCheck(request.POST)
        context.update({'form': form})

    return render(request, 'astro_check/astro_check_page.html', context=context)
