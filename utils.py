import time
import sys


color_red = "\033[31m"
color_green = "\033[32m"
color_yellow = "\033[33m"
color_blue = "\033[34m"
color_purple = "\033[35m" 
color_cyan = "\033[36m" 
color_white = "\033[37m"
color_orange = "\033[38;5;208m"
color_light_blue = "\033[38;5;153m"
color_reset = "\033[0m"


def typewriter(text, delay=0.05, color=color_reset):
    sys.stdout.write(color)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    print(color_reset)