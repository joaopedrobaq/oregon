import pyautogui
import time
import pyperclip
import json
from coords import coords

pc = 0

# Pegar do JSON
with open('processos.json', 'r') as f:
    data = json.load(f)

i = 1
for item in data:
    print(f'{i}) {item["processo"]}')
    i += 1

i = int(input("Qual processo você quer? ")) - 1

for x in range(i, i + 10):
    processo = data[x]['processo']

    anotacoes = f'''AÇÃO DE EXECUÇÃO AUTÔNOMA PROVISÓRIA, do Título Judicial decorrente do Processo nº {data[x]['origem']} 
'''
    n = 1
    for nome in data[x]['nomes']:
        anotacoes += f'''
{n}) {nome} '''
        n += 1

    # CADASTROS
    pyautogui.moveTo(coords[pc]['cadastros'])
    pyautogui.click()
    # NOVO PROCESSO
    time.sleep(0.5)
    pyautogui.moveTo(coords[pc]['novoprocesso']['cadastroProcesso'])
    pyautogui.click()

    # NUMERO PROCESSO
    time.sleep(2)
    pyautogui.moveTo(coords[pc]['novoprocesso']['numero'])
    pyautogui.click()
    pyperclip.copy(processo)
    pyautogui.hotkey('ctrl', 'v')

    # NATUREZA - TRABALHISTA
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write("T", 0.1)
    time.sleep(1)
    pyautogui.press("enter")

    # AÇÃO - TRABALHISTA
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write("T", 0.1)
    time.sleep(1)
    pyautogui.press("enter")

    # ADVOGADO - PITANGA
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write("Pedro C", 0.1)
    pyautogui.press("enter")

    # PROCEDIMENTO - ORDINARIO
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write("Ordin", 0.1)
    pyautogui.press("enter")

    # COLETIVO CHECK
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("space")

    # VALOR DA CAUSA - 70K
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.write("70.000,00")

    # ANOTAÇÕES
    pyautogui.press("tab")
    pyperclip.copy(anotacoes)
    pyautogui.hotkey('ctrl', 'v')

    # CRIAR
    pyautogui.moveTo(coords[pc]['novoprocesso']['criar'])
    pyautogui.click()

    # NOVAS PARTES
    time.sleep(1)
    pyautogui.moveTo(coords[pc]['novoprocesso']['novaParte'])
    pyautogui.click()
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.click()

    # PARTE SINDICATO - AUTOR
    pyautogui.moveTo(coords[pc]['novoprocesso']['primeiraParte'])
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(coords[pc]['busca'])
    pyautogui.click()
    pyautogui.write("Sindicato dos banc")
    pyautogui.press("enter")

    time.sleep(4)

    # Pegar primeiro resultado
    pyautogui.moveTo(coords[pc]['primeiro'])
    pyautogui.click()
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press("tab")
    pyperclip.copy("Parte")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("tab")
    pyautogui.hotkey('shift', 'tab')
    pyperclip.copy("Parte")
    pyautogui.hotkey('ctrl', 'v')
    #pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write("Autor")
    # pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("space")
    pyautogui.press("tab")

    # PARTE BANCO - RÉU
    pyautogui.moveTo(coords[pc]['novoprocesso']['segundaParte'])
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(coords[pc]['busca'])
    pyautogui.click()
    pyautogui.write("Banco do Brasil")
    pyautogui.press("enter")

    time.sleep(4)

    # Pegar primeiro resultado
    pyautogui.moveTo(coords[pc]['primeiro'])
    pyautogui.click()
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press("tab")
    pyautogui.write("Parte")
    # pyautogui.press("enter")
    pyautogui.press("tab")
    pyperclip.copy("Réu")
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.press("space")
