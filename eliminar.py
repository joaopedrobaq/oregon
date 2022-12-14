import pyautogui

print("Quer apagar quantas linhas?")
linhas = int(input()) - 1

for i in range(linhas):
    pyautogui.scroll(-100)
    pyautogui.moveTo(1000, 700)
    pyautogui.click()
    pyautogui.scroll(100000)
    pyautogui.moveTo(1400, 400)
    pyautogui.click()
