import calendar
from datetime import datetime

import jpholiday


def get_time() -> datetime:
    return datetime.now()


def get_workday(now: datetime) -> list:
    cal = calendar.Calendar()
    holidays = [day[0].day for day in jpholiday.month_holidays(now.year, now.month)]
    weekday = [
        day[0]
        for day in cal.itermonthdays2(now.year, now.month)
        if day[0] != 0 and day[1] < 5
    ]

    return [day for day in weekday if day not in holidays]


def show_info(now: datetime, workday: list) -> None:
    print(f"所定労働日数: {len(workday)} day")
    print(f"月規定労働時間: {len(workday) * 8} h")
    print(f"実働日数: {workday.index(now.day) + 1} day")
    print(f"必須労働時間: {(workday.index(now.day) + 1) * 8} h")


def show_worktime() -> None:
    now = get_time()
    workday = get_workday(now)
    show_info(now, workday)
