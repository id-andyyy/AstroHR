from django.contrib.auth.decorators import login_required

from astro_check.forms import AstroCheck
from astro_check.utils import get_role, get_team, get_asc_num, get_team_compatibility, get_company_compatibility, \
    get_compatibility_message, get_team_ascendant, get_company_ascendant
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
            role_id = int(form.cleaned_data['role_id'])
            email = form.cleaned_data['email']
            team_id = int(form.cleaned_data['team_id'])
            day = int(form.cleaned_data['day'])
            month = int(form.cleaned_data['month'])
            year = int(form.cleaned_data['year'])
            hours = int(form.cleaned_data['hours'])
            minutes = int(form.cleaned_data['minutes'])
            time_zone = int(form.cleaned_data['time_zone'])
            city = form.cleaned_data['city']

            ascendant = get_asc_num(day, month, year, city, hours, minutes, time_zone)

            team_compatibility = get_team_compatibility(team_id, ascendant)
            company_compatibility = get_company_compatibility(ascendant)

            team_message = get_compatibility_message(get_team_ascendant(team_id), ascendant, team_id, team_compatibility)
            company_message = get_compatibility_message(get_company_ascendant(), ascendant, -1, company_compatibility)

            context = {
                'title': f'Совместимость кандидата {surname} {name}',
                'name': name,
                'surname': surname,
                'patronymic': patronymic,
                'day': day,
                'month': month,
                'year': year,
                'email': email,
                'role_id': form.cleaned_data['role_id'],
                'team_id': form.cleaned_data['team_id'],
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
