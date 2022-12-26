import pyautogui
import pyperclip
import re
import time
import json
from coords import coords

pc = 4

processos = []

print("Há os seguintes processos:")
i = 1
for item in processos:
    print(f"{i}) {item}")
    i += 1
print("Por qual você quer começar?")

item_escolhido = int(input("Qual o próximo processo?")) - 1

for i in range(item_escolhido, len(processos)):
    # Clicar na Busca
    pyautogui.moveTo(coords[pc]['pje']['busca'])
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')

    # Clicar nos detalhes
    time.sleep(2)
    pyautogui.moveTo(coords[pc]['pje']['detalhes'])
    pyautogui.click()

    # Buscar e Clicar na petição inicial
    time.sleep(5)
    pyautogui.moveTo(coords[pc]['pje']['buscaFiltro'])
    pyautogui.click()
    pyautogui.write("inicial")
    pyautogui.moveTo(coords[pc]['pje']['inicial'])
    time.sleep(3)
    pyautogui.click()

    # Clicar no frame do arquivo
    time.sleep(3)
    pyautogui.moveTo(coords[pc]['pje']['frame'])
    pyautogui.click()

    # Selecionar tudo e copiar
    pyautogui.keyDown("pagedown")
    time.sleep(1.5)
    pyautogui.keyUp("pagedown")
    pyautogui.keyDown("pageup")
    time.sleep(1.5)
    pyautogui.keyUp("pageup")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')

    # Fechar aba
    pyautogui.hotkey('ctrl', 'w')

    # Apagar busca
    time.sleep(1)
    pyautogui.moveTo(coords[pc]['pje']['apagarBusca'])
    pyautogui.click()

    # parte de tratamento de dados
    string = pyperclip.paste()

    # Pegar tipo de ação com processo de origem
    string = string.replace("\n", "/")
    match = re.search(r'\d{7}\.\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}', string)
    tipo = match.group()
    print(tipo)

    # Pegar lista de nomes
    nomes = re.findall(r'\d{2}[ ]+([A-Z]+(?:[ ]+[A-Z]+)*)', string)
    print(nomes)

    # enviar dados ao json
    objeto = {"processo": processo, "origem": tipo, "nomes": nomes}

    with open('processos.json', 'r') as f:
        # Adiciona os dados ao final do arquivo JSON
        data = json.load(f)

    data.append(objeto)

    with open('processos.json', 'w') as f:
        json.dump(data, f)
