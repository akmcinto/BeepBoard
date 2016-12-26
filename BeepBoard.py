import winsound, string
# from msvcrt import getch
import pyHook, pythoncom, sys, logging

# import win32api # pypiwin32
# import win32console
# import win32gui
# import pythoncom, pyHook

# # alph = list(string.ascii_lowercase)
# # nums = list(i for i in range(len(alph)))
# # an_dict = dict(zip(alph, nums))
#ad
dur = 100
key = None
#
# while key is not 27:
#     key = ord(getch())
#     num = key - 97
#
#     if num in range(0, 26):
#         freq = 750 + (num * 25)
#         winsound.Beep(freq, dur)

def OnKeyboardEvent(event):
    key = event.Ascii
    if key is 27:
        quit()
    num = key - 97
    if key in range(97, 123):
        freq = 750 + ((key - 97) * 25)
        winsound.Beep(freq, dur)
    else if key in range(0, 26):
        freq = 750 + ((key - 65) * 25)
        winsound.Beep(freq, dur)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
