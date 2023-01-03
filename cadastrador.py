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
1) NILSON RODRIGUES SANTOS
2) NILSON SOARES DE ALMEIDA
3) NILTER CARLOS AZEVEDO DOS SANTOS
4) NILTON AMORIM DE CARVALHO
5) NILTON BONFIM LEAO
6) NILTON CARLOS TEIXEIRA DE OLIVEIRA
7) NILTON DA SILVA
8) NILTON DA SILVA LIMA
9) NILTON LEITE DE OLIVEIRA
10) NILVA DE CARVALHO MALHEIROS
11) NILVANIA COSTA SILVA
12) NILZA CIRINEU TEIXEIRA
13) NILZAN VIEIRA DO NASCIMENTO
14) NILZETE AMORIM LOURA
15) NILZETE MARIA BOMFIM
16) NINA ROSA NEVES PORTELA
17) NIUVAN PRADO PEREIRA
18) NIVALDO ALMEIDA DE SOUZA JR
19) NIVALDO COSTA LOBO
20) NIVALDO DA SILVA CARNEIRO JRx


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
