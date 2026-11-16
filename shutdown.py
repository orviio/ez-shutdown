# ██████╗ ██████╗ ██╗   ██╗██╗██╗ ██████╗
# ██╔═══██╗██╔══██╗██║   ██║██║██║██╔═══██╗
# ██║   ██║██████╔╝██║   ██║██║██║██║   ██║
# ██║   ██║██╔══██╗╚██╗ ██╔╝██║██║██║   ██║
# ╚██████╔╝██║  ██║ ╚████╔╝ ██║██║╚██████╔╝
#  ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚═╝╚═╝ ╚═════╝

import os
import platform
import sys
import time

def shutdown():
    systemos = platform.system()

    if systemos == "Windows":
        os.system("shutdown /s /t 0")

    elif systemos == "Linux":
        os.system("systemctl poweroff")

    elif systemos == "Darwin":
        os.system("""osascript -e 'tell application "System Events" to shut down'""")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear_screen()
    confirm = input("Shut down computer? Any unsaved work may be lost. y/n \n:>").strip().lower()

    if confirm == "y":
        clear_screen()
        print("\nShutdown confirmed, see ya!...")
        time.sleep(1)
        shutdown()
        sys.exit()

    elif confirm == "n":
        clear_screen()
        print("Shutdown cancelled.")
        time.sleep(1)
        sys.exit()

    else:
        print("\nUnrecognised format. Please enter y or n.")
        time.sleep(1)
        continue
