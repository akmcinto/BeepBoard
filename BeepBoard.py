import winsound, string
# http://www.instructables.com/id/Simple-Keylogger-Python/?ALLSTEPS
import pyHook, pythoncom

dur = 100
key = None

def OnKeyboardEvent(event):
    key = event.Ascii
    if key is 27:
        quit()
    if key in range(97, 123):
        freq = 600 + ((key - 97) * 35)
        winsound.Beep(freq, dur)
    elif key in range(65, 91):
        freq = 670 + ((key - 65) * 30)
        winsound.Beep(freq, dur)
    elif key in range(48, 58):
        freq = 680 + ((key - 48) * 95)
        winsound.Beep(freq, dur)
    elif key in range(32, 48):
        freq = 630 + ((key - 32) * 85)
        winsound.Beep(freq, dur)
    elif key in range(58, 65):
        freq = 700 + ((key - 58) * 105)
        winsound.Beep(freq, dur)
    elif key in range(91, 97):
        freq = 1065 + ((key - 91) * 110)
        winsound.Beep(freq, dur)
    elif key is 8:
        freq = 500
        winsound.Beep(freq, dur)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
