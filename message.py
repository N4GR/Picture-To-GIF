from text import colour
from datetime import datetime

class logging:
    def __init__(self) -> None:
        self.end = "\033[0m"

    def log(type: str, text: str):
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if type == "error":
            print(f"|{colour.BRIGHT_CYAN} {now} {colour.END}|{colour.BRIGHT_RED} ERROR {colour.END}| {text}")
        if type == "success":
            print(f"|{colour.BRIGHT_CYAN} {now} {colour.END}|{colour.BRIGHT_GREEN} SUCCESS {colour.END}| {text}")
        if type == "note":
            print(f"|{colour.BRIGHT_CYAN} {now} {colour.END}|{colour.BRIGHT_BLUE} NOTE {colour.END}| {text}")
        if type == "input":
            return input(f"|{colour.BRIGHT_CYAN} {now} {colour.END}|{colour.BRIGHT_YELLOW} INPUT {colour.END}| {text}")
