from activities.models import Activity


def weekday_string_to_choice(weekday: str) -> Activity.Weekday:
    days_dict = {
        "Monday": Activity.Weekday.MONDAY,
        "Tuesday": Activity.Weekday.TUESDAY,
        "Wednesday": Activity.Weekday.WEDNESDAY,
        "Thursday": Activity.Weekday.THURSDAY,
        "Friday": Activity.Weekday.FRIDAY,
        "Saturday": Activity.Weekday.SATURDAY,
        "Sunday": Activity.Weekday.SUNDAY,
    }
    return days_dict[weekday]