import re

from astro_check.models import Role, Team


def get_role(role_id: int) -> str:
    return Role.objects.get(pk=role_id).title


def get_team(team_id: int) -> str:
    return Team.objects.get(pk=team_id).title
