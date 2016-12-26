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
    num = key - 97
    if num in range(0, 26):
        freq = 750 + (num * 25)
        winsound.Beep(freq, dur)
    # logging.log(10,chr(event.Ascii))s
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
