```
 ██████╗ ██████╗ ██╗   ██╗██╗██╗ ██████╗
 ██╔═══██╗██╔══██╗██║   ██║██║██║██╔═══██╗
 ██║   ██║██████╔╝██║   ██║██║██║██║   ██║
 ██║   ██║██╔══██╗╚██╗ ██╔╝██║██║██║   ██║
 ╚██████╔╝██║  ██║ ╚████╔╝ ██║██║╚██████╔╝
  ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  ╚═╝╚═╝ ╚═════╝
```


Honestly, i have no idea if this thing runs or not. theoretically, on paper, it should run. But im not installing windows, nor am i paying $5000 for a mac. so those OS' are untested.

# DISCLAIMER! If this script actually works on your OS, surprise surprise, it WILL shut down your computer. SAVE YOUR WORK BEFORE RUNNING!


If anyone actually decides to run this, but they encounter any issues, try these fixes:


Windows:

If for some reason, the shutdown fails with "Access Denied," try running the terminal as administrator.
Also, if your computer is managed, they may restrict shutdown permissions. https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/


Linux: 

The script needs systemd to work.

If auth is needed, you can approve it manually.
If the shutdown is blocked itself, check the terminals error message for permission issues, or applications preventing shutdown. https://www.freedesktop.org/software/systemd/man/256/systemctl.html


macOS:

Alright you rich fucks, If you guys decide to actually read this file instead of asking claude to "fix this script no mistakes", here is how.

Allow the terminal or editor to control "System Events" when prompted.

If you denied it, check "System Settings -> Privacy & Security -> Automation"

Or, just ask claude. i know youll do it anyway.

fuck you.
```