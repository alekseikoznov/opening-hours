from typing import List

from app.schemas.openning_hours import OpeningHours


def convert_to_12_hour_format(unix_time: int) -> str:
    """Преобразованеие в 12-часовой пояс."""
    hours, minutes = divmod(int(unix_time), 3600)
    period = 'AM' if hours < 12 else 'PM'
    hours = hours % 12 or 12
    minutes = minutes // 60
    if minutes:
        return f"{hours}:{minutes:02d} {period}"
    return f"{hours} {period}"


def format_opening_hours(week: List) -> dict:
    """Форматирование дней и времени."""
    formatted_opening_hours = {}
    formatted_hours = []
    open_time = None
    close_time = None

    for day in week:
        current_day = day[0]
        if len(day) == 1:
            formatted_opening_hours[current_day.capitalize()] = 'Closed'
        else:
            for hour in day[1:]:
                if not open_time:
                    open_time = convert_to_12_hour_format(hour)
                else:
                    close_time = convert_to_12_hour_format(hour)
                    formatted_hours.append(f"{open_time} - {close_time}")
                    open_time = None
                    close_time = None
            formatted_opening_hours[
                current_day.capitalize()
            ] = ', '.join(formatted_hours)
            formatted_hours = []
    return formatted_opening_hours


def week_opening_hour(data: OpeningHours) -> dict:
    """Корректное соотношение дней и времени работы."""
    week = []
    index_day = 0
    monday_close = None

    for day, hours in data.dict().items():
        week.append([day])
        for hour in hours:
            if len(week[index_day]) == 1 and hour['type'] == 'close':
                if index_day == 0:  # если закрытие воскресенья в понедельник
                    monday_close = hour['value']
                else:
                    week[index_day - 1].append(hour['value'])
            else:
                week[index_day].append(hour['value'])
        index_day += 1
    if monday_close:
        week[-1].append(monday_close)
    return format_opening_hours(week)
