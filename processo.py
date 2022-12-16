import pyautogui
import time

pc = 1

if pc == 1:
    #Coordenadas PC Estagiário
    busca = (180, 180)
    executar = (190, 390)
    abrir = (460, 185)
    anotacoes = (1000, 350)
    primeiraLinha = (500, 520)
    quantidade = 3

if pc == 2:
    # Coordenadas PC Angela
    teste = ""

pyautogui.moveTo(busca)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")

pyautogui.moveTo(executar)
pyautogui.click()

time.sleep(1.5)

pyautogui.moveTo(abrir)
pyautogui.click()

time.sleep(5)

#pyautogui.moveTo(anotacoes)
#pyautogui.click()
#pyautogui.hotkey('ctrl', 'c')

pyautogui.moveTo(primeiraLinha)
for i in range(quantidade):
  pyautogui.click()
  pyautogui.click()
  pyautogui.move(0, 25)
  time.sleep(0.2)

pyautogui.scroll(-300)