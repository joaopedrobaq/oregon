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
pyautogui.write()

pyautogui.move(0, 50)
pyautogui.click()
pyautogui.write("Física")
pyautogui.press("enter")

pyautogui.move(0, 50)
pyautogui.click()
pyautogui.write("Parte")
pyautogui.press("enter")

