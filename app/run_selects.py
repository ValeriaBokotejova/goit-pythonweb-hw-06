import argparse

from colorama import Fore, init
from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
    select_11,
    select_12,
)

init(autoreset=True)

SELECTS = {
    "select_1": {"func": select_1, "args": []},
    "select_2": {"func": select_2, "args": ["subject_id"]},
    "select_3": {"func": select_3, "args": ["subject_id"]},
    "select_4": {"func": select_4, "args": []},
    "select_5": {"func": select_5, "args": ["teacher_id"]},
    "select_6": {"func": select_6, "args": ["group_id"]},
    "select_7": {"func": select_7, "args": ["group_id", "subject_id"]},
    "select_8": {"func": select_8, "args": ["teacher_id"]},
    "select_9": {"func": select_9, "args": ["student_id"]},
    "select_10": {"func": select_10, "args": ["student_id", "teacher_id"]},
    "select_11": {"func": select_11, "args": ["student_id", "teacher_id"]},
    "select_12": {"func": select_12, "args": ["group_id", "subject_id"]},
}


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--name", help="Select function name (select_1 to select_12)"
    )
    parser.add_argument("--student_id", type=int)
    parser.add_argument("--teacher_id", type=int)
    parser.add_argument("--subject_id", type=int)
    parser.add_argument("--group_id", type=int)
    parser.add_argument("--list", action="store_true", help="List available queries")

    args = parser.parse_args()

    if args.list:
        print(Fore.YELLOW + "\nAvailable queries:")
        for key, val in SELECTS.items():
            print(Fore.CYAN + f"{key}: args = {val['args']}")
        return

    if args.name not in SELECTS:
        print(Fore.RED + "✘ Invalid select function name. Use --list to see options.")
        return

    func_data = SELECTS[args.name]
    try:
        kwargs = {arg: getattr(args, arg) for arg in func_data["args"]}
        result = func_data["func"](**kwargs)

        # Display results
        if isinstance(result, list):
            if not result:
                print(Fore.YELLOW + "No results found.")
            else:
                for row in result:
                    print(Fore.CYAN + str(row))
        elif result is None:
            print(Fore.YELLOW + "No result.")
        else:
            print(Fore.GREEN + str(result))

    except TypeError as e:
        print(Fore.RED + f"✘ Missing arguments: {e}")
    except Exception as e:
        print(Fore.RED + f"✘ Error while executing: {e}")


if __name__ == "__main__":
    run()
