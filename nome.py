import pyautogui
import time

pyautogui.moveTo(40, 100)
pyautogui.click()

time.sleep(0.5)
pyautogui.moveTo(40, 140)
pyautogui.click()

time.sleep(1)
pyautogui.moveTo(400, 350)
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

pyautogui.moveTo(490,685)
pyautogui.click()