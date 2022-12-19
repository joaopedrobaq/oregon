import pyautogui
import time
from coords import coords

pc = 3

pyautogui.moveTo(coords[pc]['cadastros'])
pyautogui.click()

time.sleep(0.5)
pyautogui.moveTo(coords[pc]['novaPessoa'])
pyautogui.click()

time.sleep(1)
pyautogui.moveTo(coords[pc]['nomePessoa'])
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')

pyautogui.move(0, 50)
pyautogui.click()
time.sleep(0.5)
pyautogui.write("F", 0.1)
pyautogui.press("enter")

pyautogui.move(0, 50)
pyautogui.click()
time.sleep(0.5)
pyautogui.write("P", 0.1)
pyautogui.press("enter")

time.sleep(0.5)
pyautogui.moveTo(coords[pc]['salvarPessoa'])
pyautogui.click()