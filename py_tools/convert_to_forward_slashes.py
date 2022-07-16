from tkinter import Tk
import winsound

# Using Tk window since it has handy platform unspecific utility functions for the clipboard
window = Tk()
# Disable window that pops up
window.withdraw()

text = window.clipboard_get()

# Find and replace backslashes to forward slashes if there are any
has_backslashes = text and text.find("\\") >= 0

if has_backslashes:
    new_text = text.replace("\\", "/")

    window.clipboard_clear()
    window.clipboard_append(new_text)
    window.update()

    winsound.MessageBeep()
else:
    # Play fail sound
    winsound.MessageBeep(winsound.MB_ICONHAND)

window.destroy()
