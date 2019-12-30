import pyperclip
import pyautogui, time
numbers = ''
for index in range(200):
    numbers += str(index) + '\n'
print(pyperclip.copy(numbers))

time.sleep(2);
print(pyautogui.scroll(200))