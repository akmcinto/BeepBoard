import winsound, string
from msvcrt import getch

# alph = list(string.ascii_lowercase)
# nums = list(i for i in range(len(alph)))
# an_dict = dict(zip(alph, nums))

dur = 100
key = None

while key is not 27:
    key = ord(getch())
    num = key - 97

    if num in range(0, 26):
        freq = 750 + (num * 25)
        winsound.Beep(freq, dur)
