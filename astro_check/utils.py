import math
from datetime import timedelta, datetime
import ssl
import certifi
from geopy.geocoders import Nominatim

from astro_check.models import Role, Team, Worker


def get_role(role_id: int) -> str:
    return Role.objects.get(pk=role_id).title


def get_team(team_id: int) -> str:
    return Team.objects.get(pk=team_id).title


def get_location_by_address(address):
    context = ssl.create_default_context(cafile=certifi.where())
    geolocator = Nominatim(user_agent="city_coordinates", ssl_context=context)
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return 0, 0


def get_day_of_year(day: int, month: int, year: int) -> int:
    try:
        date_object = datetime(year, month, day)
        day_of_year = date_object.timetuple().tm_yday
        return day_of_year
    except ValueError as e:
        return 1


def get_asc_num(day, month, year, address, hour, minute, zone):
    x = 110
    asc_num = 0

    location = get_location_by_address(address)
    latitude = float(location[0])
    longitude = float(location[1])

    day_of_year = get_day_of_year(day, month, year)

    time_min = minute
    time_zone = zone
    time_GMT_h = 12 - time_zone
    time_GMT_m = time_min
    time_now = time_zone * 15
    time_MCT = timedelta(hours=12, minutes=time_GMT_m) - timedelta(minutes=(time_now - longitude) * 4)
    time_MCT_minutes = time_MCT.total_seconds() / 60

    a1 = 15 * (time_MCT_minutes - 12)
    a2 = (72 * day_of_year - 5814) / 73
    a3 = math.asin(math.sin(a2) * math.sin(23.5))
    a4 = math.cos(a1) * math.cos(a3) * math.cos(latitude)
    a5 = math.sin(a3) * math.sin(latitude)
    y = math.fabs(math.asin(a4 + a5))

    asc_val = int((252 + latitude) / y)
    if asc_val > 360:
        asc_val = math.fabs(asc_val - 360 * int(asc_val / 360))
        if asc_val > 360:
            asc_val = math.fabs(asc_val - x)

    if 0 < asc_val < 30:
        asc_num = 1
    if 30 < asc_val < 60:
        asc_num = 2
    if 60 < asc_val < 90:
        asc_num = 3
    if 90 < asc_val < 120:
        asc_num = 4
    if 120 < asc_val < 150:
        asc_num = 5
    if 150 < asc_val < 180:
        asc_num = 6
    if 180 < asc_val < 210:
        asc_num = 7
    if 210 < asc_val < 240:
        asc_num = 8
    if 240 < asc_val < 270:
        asc_num = 9
    if 270 < asc_val < 300:
        asc_num = 10
    if 300 < asc_val < 330:
        asc_num = 11
    if 330 < asc_val < 360:
        asc_num = 12
    return asc_num


def get_compatibility(ascendant_1: int, ascendant_2: int) -> int:
    compatibility_dict = {
        1: {
            1: 97,
            2: 23,
            3: 64,
            4: 52,
            5: 83,
            6: 9,
            7: 50,
            8: 76,
            9: 95,
            10: -100,
            11: 81,
            12: 0,
        },
        2: {
            1: -93,
            2: 90,
            3: -34,
            4: 71,
            5: -15,
            6: 89,
            7: 78,
            8: 5,
            9: 21,
            10: 86,
            11: -15,
            12: 70,
        },
        3: {
            1: 64,
            2: -30,
            3: 99,
            4: -41,
            5: 97,
            6: -33,
            7: 100,
            8: -11,
            9: 88,
            10: 2,
            11: 94,
            12: 37,
        },
        4: {
            1: -44,
            2: 85,
            3: -43,
            4: 90,
            5: -51,
            6: 74,
            7: 50,
            8: 71,
            9: -89,
            10: -100,
            11: -45,
            12: 82,
        },
        5: {
            1: 99,
            2: -100,
            3: 46,
            4: -98,
            5: 91,
            6: -84,
            7: 75,
            8: -39,
            9: 84,
            10: -91,
            11: -4,
            12: -18,
        },
        6: {
            1: -100,
            2: 99,
            3: -87,
            4: 79,
            5: 0,
            6: 100,
            7: 16,
            8: 35,
            9: 44,
            10: 92,
            11: -96,
            12: 87,
        },
        7: {
            7: 98,
        },
        8: {
            8: 88,
        },
        9: {
            9: 88,
        },
        10: {
            10: 100,
        },
        11: {
            11: 75,
        },
        12: {
            12: 100,
        },
    }

    if ascendant_1 > ascendant_2:
        ascendant_1, ascendant_2 = ascendant_2, ascendant_1

    return compatibility_dict[ascendant_1][ascendant_2]


def get_team_compatibility(team_id: int, ascendant: int) -> int:
    team_workers = Worker.objects.filter(team=team_id)
    compatibility = 0

    for worker in team_workers:
        worker_ascendant = worker.ascendant
        compatibility += get_compatibility(worker_ascendant, ascendant)

    if len(team_workers) != 0:
        compatibility /= len(team_workers)

    return round(compatibility)


def get_company_compatibility(ascendant: int) -> int:
    workers = Worker.objects.all()
    compatibility = 0

    for worker in workers:
        worker_ascendant = worker.ascendant
        compatibility += get_compatibility(worker_ascendant, ascendant)

    if len(workers) != 0:
        compatibility /= len(workers)

    return round(compatibility)


def get_team_message(ascendant: int, team_compatibility: int) -> str:
    return


def get_company_message(ascendant: int, company_compatibility: int) -> str:
    return
