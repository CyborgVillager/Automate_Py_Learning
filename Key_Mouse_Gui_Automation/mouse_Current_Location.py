import pyautogui
pyautogui.FAILSAFE = True
# This program displays the mouse's current position
print('Press Ctr-C to quit the program.')

try:
    while True:
        x,y = pyautogui.position()
        position_String = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(position_String, end='')
        print('\b' * len(position_String), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone')