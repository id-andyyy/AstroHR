from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='фамилия')
    patronymic = models.CharField(max_length=100, verbose_name='отчество')
    date_of_birth = models.DateField(verbose_name='дата рождения')
    email = models.EmailField(verbose_name='почта')
    role = models.ForeignKey('Role', on_delete=models.PROTECT, verbose_name='роль')
    team = models.ForeignKey('Team', on_delete=models.PROTECT, verbose_name='команда')
    team_compatibility = models.IntegerField(verbose_name='совместимость с командой')
    company_compatibility = models.IntegerField(verbose_name='совместимость с компанией')
    data_joined = models.DateField(auto_now_add=True, verbose_name='дата присоединения')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        db_table = 'workers'
        verbose_name = 'работник'
        verbose_name_plural = 'работники'
        ordering = ['-data_joined', 'id']


class Role(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'roles'
        verbose_name = 'роль'
        verbose_name_plural = 'роли'
        ordering = ['title']


class Team(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'teams'
        verbose_name = 'команда'
        verbose_name_plural = 'команды'
        ordering = ['title']
