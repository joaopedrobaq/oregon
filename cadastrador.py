import re
import time
import pyautogui
import pyperclip
from coords import coords

#Editar o Valor de Acordo com o PC usado
# 0 = Estagiário
# 1 = Angela
# 2 = João Porto
# 3 = Bartira
pc = 3

# String para extrair os nomes
string = """
1) EDERSON PEREIRA SANTOS
2) EDESIO EVARISTO DOS SANTOS JUNIOR
3) EDGAR SANTIAGO VIANA NETO
4) EDGAR SEVERIANO DE ALMEIDA
5) EDGARD DANTAS DE SOUZA
6) EDGARD GONCALVES S OLIVEIRA
7) EDGARD RIBEIRO GUIMARAES NETO
8) EDI TACITO ALMEIDA R SOUZA
9) EDIANA SALES LELES
10) EDIELSON DOURADO DOS SANTOS
11) EDILBERTO TEIXEIRA PIRES
12) EDILEIA CAMPOS SANTOS
13) EDILEIDE ALVES SANTANA
14) EDILENE BARROS ARAUJO
15) EDILENE GONZAGA ALVES RIBEIRO
16) EDILENE SANTOS BARRETO MENEZES
17) EDILENE SANTOS SILVA
18) EDILEUZA ALVES SANTANA
19) EDILMA DANTAS RODRIGUES SCHADE
20) EDILMA SILVA DE ARAUJO



"""

# Extrair os nomes e transformar em array
# padrão antigo - nomes = re.findall(r"\d+\) (.*)", string)
regex = r'\d+\s+(.+)'
nomes = re.findall(regex, string)
nomes = [nome.strip() for nome in nomes]

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
