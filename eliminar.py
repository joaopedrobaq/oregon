import pyautogui

pc = 1

if pc == 1:
    #Coordenadas PC Estagiário
    linha = (1000, 515)
    apagar = (1085, 420)

if pc == 2:
    # Coordenadas PC Angela
    linha = (1000, 700)
    apagar = (1400, 400)

print("Quer apagar quantas linhas?")
linhas = int(input()) - 1

for i in range(linhas):
    pyautogui.scroll(-100000)
    pyautogui.moveTo(linha)
    pyautogui.click()
    pyautogui.scroll(100000)
    pyautogui.moveTo(apagar)
    pyautogui.click()
