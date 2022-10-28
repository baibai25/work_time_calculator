import argparse

from .calc_diff import calc_diff
from .show_worktime import show_worktime


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hour", type=int, help="worked hour", required=False)
    parser.add_argument("--time", type=int, help="worked time", required=False)

    return parser.parse_args()


# main()
def main():
    show_worktime()

    args = parser()
    if args.hour != None and args.time != None:
        calc_diff(args.hour, args.time)


if __name__ == "__main__":
    main()
