import pyautogui
import pyperclip
import re
import time
from coords import coords

pc = 4

processo = '0000732-35.2022.5.05.0037'

pyperclip.copy(processo)

# parte de interação com tela

# Clicar na Busca
pyautogui.moveTo(coords[pc]['pje']['busca'])
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')

# Clicar nos detalhes
time.sleep(2)
pyautogui.moveTo(coords[pc]['pje']['detalhes'])
pyautogui.click()

# Clicar na petição inicial
time.sleep(5)
pyautogui.moveTo(coords[pc]['pje']['inicial'])
pyautogui.click()

# Clicar no frame do arquivo
time.sleep(4)
pyautogui.moveTo(coords[pc]['pje']['frame'])
pyautogui.click()

# Selecionar tudo e copiar
pyautogui.keyDown("pagedown")
time.sleep(1)
pyautogui.keyUp("pagedown")
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')

# parte de tratamento de dados
# Pegar tipo de ação com processo de origem
# Pegar lista de nomes
# montar string com ambos para anotações no oregon
