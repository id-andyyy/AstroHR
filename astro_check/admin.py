from django.contrib import admin

from .models import Worker, Role, Team


@admin.register(Worker)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'patronymic', 'role', 'team', 'team_compatibility']
    list_display_links = ['name', 'surname', 'patronymic']
    ordering = ['-data_joined']
    list_filter = ['role__title', 'team__title']
    search_fields = ['name', 'surname', 'patronymic']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    ordering = ['title']
    search_fields = (['title'],)


@admin.register(Team)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    ordering = ['title']
    search_fields = ['title']
