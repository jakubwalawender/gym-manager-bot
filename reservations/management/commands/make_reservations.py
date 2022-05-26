from datetime import timedelta
from enum import Enum

import requests
from django.core.management import BaseCommand
from accounts.models import User
from config.settings import RESERVATION_URL, REMOVE_RESERVATION_URL
from django.utils import timezone
from reservations.management.get_token import get_token


class Command(BaseCommand):
    help = 'Makes all desired reservations'

    def handle(self, *args, **options):
        for user in User.objects.all():
            token = get_token(user.gym_manager_login, user.gym_manager_password)
            while timezone.localtime(timezone.now()).hour != 0:
                pass
            self.make_reservations(user, token)
        print(f"Done!")

    def make_reservations(self, user, token):
        headers = {
            "Authorization": f"Bearer {token}",
        }
        for reservation in user.reservations.all():
            reservation_date = (timezone.localtime(timezone.now()) + timedelta(days=7)).date().strftime("%Y-%m-%d")
            reservation_datetime = f"{reservation_date}T{reservation.hour}Z"
            data = {
                "UserId": user.gym_manager_id,
                "Date": reservation_datetime,
                "ClassScheduleId": reservation.activity_id
            }

            r = requests.post(RESERVATION_URL, json=data, headers=headers)
            if r.status_code == 200:
                if r.json()["Status"] == ReservationStatus.RESERVE.value:
                    for another_option in reservation.another_reservation_options.all():
                        requests.post(REMOVE_RESERVATION_URL, json=data, headers=headers)
                        reservation_datetime = f"{reservation_date}T{another_option.hour}Z"
                        data = {
                            "UserId": user.gym_manager_id,
                            "Date": reservation_datetime,
                            "ClassScheduleId": another_option.activity_id
                        }
                        r = requests.post(RESERVATION_URL, json=data, headers=headers)
                        if r.json()["Status"] == ReservationStatus.OK.value:
                            break


class ReservationStatus(Enum):
    OK = 1
    RESERVE = 2
    DATE_TOO_FAR = -2
    ALREADY_RESERVED = -6
