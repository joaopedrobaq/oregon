import pyautogui
import pyperclip
import time
from coords import coords


def selectProcesso(pc, processo):

    pyautogui.moveTo(coords[pc]['buscaProcesso'])
    pyautogui.click()
    pyautogui.write(processo)
    pyautogui.press("enter")

    pyautogui.moveTo(coords[pc]['executarBusca'])
    pyautogui.click()

    time.sleep(1.5)

    pyautogui.moveTo(coords[pc]['abrirProcesso'])
    pyautogui.click()

    time.sleep(5)

    #pyautogui.moveTo(coords[pc]['anotacoesProcesso'])
    #pyautogui.click()
    #pyautogui.hotkey('ctrl', 'c')

    pyautogui.moveTo(coords[pc]['primeiraLinha'])
    for i in range(coords[pc]['quantidadeLinhas']):
        pyautogui.click()
        pyautogui.click()
        pyautogui.move(0, 25)
        time.sleep(0.2)

    pyautogui.scroll(-300)


# selectProcesso(0, pyperclip.paste())