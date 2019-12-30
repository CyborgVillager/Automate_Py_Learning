import pyautogui, time
pyautogui.FAILSAFE = True
time.sleep(2)
# pyautogui.click(10,5)
"""""
.mouseDown()
.mouseUp()
.doubleClikc()
.rightClick()
.middleClick()
.dragTo()
"""""
# Drag the mouse
pyautogui.click()
mouse_distance = 100
while mouse_distance > 0:
    pyautogui.dragRel(mouse_distance,0,duration=.2) #mve right
    mouse_distance -= 5
    pyautogui.dragRel(-mouse_distance, 0, duration=.2)  # mv left
    mouse_distance -= 5
    pyautogui.dragRel(0,mouse_distance,duration=.2) #mv down
    pyautogui.dragRel(0,-mouse_distance,duration=.2) #mv up