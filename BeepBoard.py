import winsound, string
# http://www.instructables.com/id/Simple-Keylogger-Python/?ALLSTEPS
import pyHook, pythoncom

dur = 100
key = None

def OnKeyboardEvent(event):
    key = event.Ascii
    print(key)
    if key is 27:
        quit()
    if key in range(97, 123):
        freq = 650 + ((key - 97) * 50)
        winsound.Beep(freq, dur)
    elif key in range(65, 91):
        freq = 710 + ((key - 65) * 20)
        winsound.Beep(freq, dur)
    elif key in range(48, 58):
        freq = 680 + ((key - 48) * 95)
        winsound.Beep(freq, dur)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
