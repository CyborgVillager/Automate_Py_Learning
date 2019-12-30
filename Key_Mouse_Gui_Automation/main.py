import pyautogui
pyautogui.PAUSE
pyautogui.FAILSAFE = True
# prints your screen size
#print(pyautogui.size())

# Auto move the mouse snakish pattern
"""""
for index in range(10):
    pyautogui.move(50,50, duration=0.25)
    pyautogui.move(50,-50, duration=0.25)
"""""

# .moveRel moves the cursor relative to its curr.position
for index in range(5):
    pyautogui.moveRel(100,0, duration=.25)
    pyautogui.moveRel(0,100, duration=.25)
    pyautogui.moveRel(-100,0, duration=.25)
    pyautogui.moveRel(0,-100, duration=.25)