from .show_worktime import get_time, get_workday


def calc_time_diff(diff):
    diff_hour = diff // 60
    diff_time = diff - diff_hour * 60

    return diff_hour, diff_time


def show_diff(worked_time, required_time):
    if worked_time < required_time:
        diff = required_time - worked_time
        diff_hour, diff_time = calc_time_diff(diff)
        print(f"差分: -{diff_hour}時間{diff_time}分")
    elif required_time < worked_time:
        diff = worked_time - required_time
        diff_hour, diff_time = calc_time_diff(diff)
        print(f"差分: +{diff_hour}時間{diff_time}分")
    else:
        print("error handling")


def calc_diff(hour, time):
    now = get_time()
    workday = get_workday(now)
    required_time = (workday.index(now.day) + 1) * 8 * 60
    worked_time = (hour * 60) + time
    show_diff(worked_time, required_time)
