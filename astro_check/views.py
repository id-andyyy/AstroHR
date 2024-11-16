from datetime import date

from django.contrib.auth.decorators import login_required

from astro_check.forms import AstroCheck, Generate
from astro_check.mail import email_go
from astro_check.models import Worker
from astro_check.utils import get_asc_num, get_team_compatibility, get_company_compatibility, \
    get_compatibility_message, get_team_ascendant, get_company_ascendant, get_ascendant_name, get_recommendations, \
    get_team, get_ascendant_titles
from django.shortcuts import render, redirect


def main(request):
    context = {
        'title': 'AstroHR',
    }
    return render(request, 'astro_check/main.html', context)


def astro_check(request):
    context = {
        'title': 'Проверка на совместимость',
    }
    if request.method == 'POST' and 'first_form' in request.POST:
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

            team_message = get_compatibility_message(get_team_ascendant(team_id), ascendant, team_id,
                                                     team_compatibility)
            company_message = get_compatibility_message(get_company_ascendant(), ascendant, -1, company_compatibility)

            context = {
                'title': f'Совместимость кандидата {surname} {name}',
                'name': name,
                'surname': surname,
                'patronymic': patronymic,
                'ascendant': ascendant,
                'ascendant_text': get_ascendant_name(ascendant),
                'team_compatibility': team_compatibility,
                'team_message': team_message,
                'company_compatibility': company_compatibility,
                'company_message': company_message,
            }

            request.session['name'] = name
            request.session['surname'] = surname
            request.session['patronymic'] = patronymic
            request.session['ascendant'] = ascendant
            request.session['role_id'] = role_id
            request.session['team_id'] = team_id
            request.session['email'] = email
            request.session['day'] = day
            request.session['month'] = month
            request.session['year'] = year
            request.session['team_compatibility'] = team_compatibility
            request.session['company_compatibility'] = company_compatibility

            return render(request, 'astro_check/astro_result_page.html', context)
        else:
            context.update({'form': form})
    elif request.method == 'POST' and 'second_form' in request.POST:
        if request.user.is_authenticated:
            name = request.session['name']
            surname = request.session['surname']
            patronymic = request.session['patronymic']
            ascendant = request.session['ascendant']
            role_id = request.session['role_id']
            team_id = request.session['team_id']
            email = request.session['email']
            day = request.session['day']
            month = request.session['month']
            year = request.session['year']
            team_compatibility = request.session['team_compatibility']
            company_compatibility = request.session['company_compatibility']

            pressed_button = request.POST.get('second_form')
            checkbox_value = request.POST.get('checkbox_field', None)

            if pressed_button == 'confirm':
                Worker(
                    name=name,
                    surname=surname,
                    patronymic=patronymic,
                    date_of_birth=date(year, month, day),
                    email=email,
                    role_id=role_id,
                    team_id=team_id,
                    ascendant=ascendant,
                    team_compatibility=team_compatibility,
                    company_compatibility=company_compatibility
                ).save()

                if checkbox_value:
                    email_go(True, email, f'{name} {surname}')
            else:
                if checkbox_value:
                    email_go(False, email, f'{name} {surname}')

        return redirect('astro_check')
    else:
        form = AstroCheck(request.POST)
        context.update({'form': form})

    return render(request, 'astro_check/astro_check_page.html', context=context)


@login_required()
def generate(request):
    context = {
        'title': 'Генерация рекомендаций',
        'generated': False,
    }
    if request.method == 'POST':
        form = Generate(request.POST)
        if form.is_valid():
            team_id = form.cleaned_data['team_id']
            context['generated'] = True
            context.update({'recommendations': get_recommendations(get_team(team_id), get_team_ascendant(team_id))})
            context.update({'form': form})
            return render(request, 'astro_check/generate_page.html', context)

    else:
        form = Generate(request.POST)
        context.update({'form': form})

    return render(request, 'astro_check/generate_page.html', context)
