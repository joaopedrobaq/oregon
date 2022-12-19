import re
import pyautogui
import pyperclip
import time
from coords import coords


def tratarLista(string):
    regex = r'\d+\s+(.+)'
    nomes = re.findall(regex, string)
    nomes = [nome.strip() for nome in nomes]
    return nomes

def cadastrador(pc, nomes):
    print("Nomes na Lista:")
    i = 1
    for nome in nomes:
        print(f"{i}) {nome}")
        i += 1
    print(f"Há um total de {len(nomes)} nomes. Em qual deseja iniciar?")
    inicio = int(input()) - 1

    # Iterar pelo Array e fazer o cadastro
    for i in range(inicio, len(nomes)):
        # Fazer o que quer com cada nome
        print(f"{i+1}) {nomes[i]}")
        pyperclip.copy(nomes[i])

        # Clicar no ...
        pyautogui.moveTo(coords[pc]['abrir'])
        pyautogui.click()

        time.sleep(2)

        # Clicar na busca
        pyautogui.moveTo(coords[pc]['busca'])
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")

        time.sleep(4)

        # Pegar primeiro resultado
        pyautogui.moveTo(coords[pc]['primeiro'])
        pyautogui.click()
        pyautogui.click()

        # Colocar como Parte
        time.sleep(1)
        pyautogui.moveTo(coords[pc]['parte'])
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write("Parte")
        pyautogui.press("enter")

        #Colocar como Autor
        time.sleep(0.5)
        pyautogui.move(130, 0)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.write("Autor")
        pyautogui.press("enter")

        # Rolar tela
        pyautogui.scroll(-300)

        # Abrir mais um
        pyautogui.moveTo(coords[pc]['novo'])
        pyautogui.click()
        pyautogui.click()

        time.sleep(0.5)

        # Rolar tela
        pyautogui.scroll(-300)
