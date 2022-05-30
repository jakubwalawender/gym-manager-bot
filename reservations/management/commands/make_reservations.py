from datetime import timedelta, datetime
from enum import Enum
import requests
from django.core.management import BaseCommand
from accounts.models import User
from config.settings import RESERVATION_URL, REMOVE_RESERVATION_URL
from reservations.management.get_token import get_token
from reservations.management.weekday_string_to_choice import weekday_string_to_choice
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Makes all desired reservations'

    def handle(self, *args, **options):
        users = []
        now = datetime.now()
        weekday = weekday_string_to_choice(now.strftime('%A'))
        logger.info(f"MAKING RESERVATIONS!\n")
        for user in User.objects.all():
            token = get_token(user.gym_manager_login, user.gym_manager_password)
            if token is None:
                logger.info(f"{user.username} User token was none. Skipping!")
                continue
            users.append({'user': user, 'token': token})

        logger.info(f"All users logged in! Waiting for desired hour...")
        while True:
            now = datetime.now()
            minutes = now.minute
            if minutes == 30 or minutes == 0:
                break
        self.make_reservations(users, weekday, datetime.strftime(datetime.now(), "%H:%M"))
        logger.info(f"RESERVING FINISHED!\n")

    def make_reservations(self, users, weekday, reservation_hour):
        for instance in users:
            user = instance['user']
            token = instance['token']

            headers = {
                "Authorization": f"Bearer {token}",
            }
            reservations = user.reservations.filter(weekday=weekday, hour=reservation_hour).order_by("-hour")
            logger.info(f"{user.username} Found {len(reservations)} desired reservations!")
            for reservation in reservations:
                reservation_date = (datetime.now() + timedelta(days=7)).date().strftime("%Y-%m-%d")
                reservation_datetime = f"{reservation_date}T{reservation.hour}Z"
                data = {
                    "UserId": user.gym_manager_id,
                    "Date": reservation_datetime,
                    "ClassScheduleId": reservation.activity_id
                }

                r = requests.post(RESERVATION_URL, json=data, headers=headers)
                if r.status_code == 200:
                    if r.json()["Status"] == ReservationStatus.RESERVE.value:
                        logger.info(f"{user.username} Seeking for some reserve")
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
                                logger.info(f"{user.username} Found reservation in reserve and made a reservation!")
                                break
                    else:
                        logger.info(f"{user.username} Reservation status code was 200 {r.json()}. Should be OK!")
                else:
                    logger.info(f"{user.username} Reservation status code was {r.status_code}! {r.json()}")


class ReservationStatus(Enum):
    OK = 1
    RESERVE = 2
    DATE_TOO_FAR = -2
    ALREADY_RESERVED = -6
