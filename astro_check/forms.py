from calendar import month
from datetime import datetime

from django import forms

from astro_check.models import Role, Team


class AstroCheck(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    surname = forms.CharField(label='Фамилия', max_length=100)
    patronymic = forms.CharField(label='Отчество', max_length=100)
    role = forms.ChoiceField(
        label='Должность',
        choices=[(role.id, role.title) for role in Role.objects.all()],
        widget=forms.Select
    )
    email = forms.EmailField(label='Почта')
    team = forms.ChoiceField(
        label='Команда',
        choices=[(team.id, team.title) for team in Team.objects.all()],
        widget=forms.Select
    )
    day = forms.ChoiceField(
        label='Дата',
        choices=[(i, i) for i in range(1, 31 + 1)],
        widget=forms.Select
    )
    month = forms.ChoiceField(
        label='Месяц',
        choices=[(i + 1, month) for i, month in enumerate(['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                 'Ноябрь', 'Декабрь'])],
        widget=forms.Select
    )
    year = forms.ChoiceField(
        label='Год',
        choices=[(i, i) for i in range(datetime.now().year - 150, datetime.now().year + 1)],
        widget=forms.Select
    )
    hours = forms.ChoiceField(
        label='Часы',
        choices=[(i, i) for i in range(0, 23 + 1)],
        widget=forms.Select
    )
    minutes = forms.ChoiceField(
        label='Минуты',
        choices=[(i, i) for i in range(0, 59 + 1)],
        widget=forms.Select
    )
    time_zone = forms.ChoiceField(
        label='Часовой пояс',
        choices=[(i, f'GMT+{i}') for i in range(0, 23 + 1)],
        widget=forms.Select
    )
    city = forms.CharField(label='Город рождения', max_length=100)
