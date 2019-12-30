import pyautogui

image = pyautogui.screenshot()
# aquire RGB color on screen
print(image.getpixel((0, 0)))
print(image.getpixel((-500,200)))
