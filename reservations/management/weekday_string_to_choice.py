from reservations.models import PossibleReservation


def weekday_string_to_choice(weekday):
    days_dict = {
        "Monday": PossibleReservation.Weekday.MONDAY,
        "Tuesday": PossibleReservation.Weekday.TUESDAY,
        "Wednesday": PossibleReservation.Weekday.WEDNESDAY,
        "Thursday": PossibleReservation.Weekday.THURSDAY,
        "Friday": PossibleReservation.Weekday.FRIDAY,
        "Saturday": PossibleReservation.Weekday.SATURDAY,
        "Sunday": PossibleReservation.Weekday.SUNDAY,
    }
    return days_dict[weekday]