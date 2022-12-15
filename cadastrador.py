import re
import time
import pyautogui
import keyboard
import pyperclip

pc = 1

if pc == 1:
    #Coordenadas PC Estagiário
    abrir = (310, 520)
    busca = (846, 215)
    primeiro = (430, 245)
    parte = (460, 520)
    novo = (310, 600)

if pc == 2:
    # Coordenadas PC Angela
    abrir = (385, 490)
    busca = (1000, 280)
    primeiro = (650, 310)
    parte = (540, 490)
    novo = (300, 720)

# String para extrair os nomes
string = """Processo nº 0001173.16.2012.5.05.0021

1) GEORGE ROBSON GUIMARAES DE MELO 
2) GEORGE RODRIGUES NEVES 
3) GEORGIA EVANGELISTA BEZERRA 
4) GEOVANE MORAES NUNES 
5) GERALDO DE OLIVEIRA UMA 
6) GERALDO EUGENIO ALVES GALINDO 
7) GERALDO RIBEIRO NEVES 
8) GERSIKA FAKIRRA DE OUVEIRA NUNES 
9) GERUSA SOUZA NASCIMENTO MATOS 
10) GERVAN DE OLIVEIRA COSTA 
11) GESSE CAMPOS RODRIGUES JUNIOR 
12) GETULIO RODRIGUES COSTA 
13) GEZIVALDO OLIVEIRA ANDRADE 
14) GILBERTO ABEL COTRIM 
15) GILBERTO MACIEL JUSTI 
16) GILCIANE DE ANDRADE LIMA 
17) GILDASIO PIRES DE OLIVEIRA 
18) GILKA MARIA BASTOS DE A GOES 
19) GILMAR DE OLIVEIRA COSTA 
20) GILSIMAR SOUZA E SILVA PEREIRA 
"""

# Extrair os nomes e transformar em array
nomes = re.findall(r"\d+\) (.*)", string)
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
    pyautogui.moveTo(abrir)
    pyautogui.click()

    time.sleep(2)

    # Clicar na busca
    pyautogui.moveTo(busca)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")

    time.sleep(4)

    # Pegar primeiro resultado
    pyautogui.moveTo(primeiro)
    pyautogui.click()
    pyautogui.click()

    # Colocar como Parte
    time.sleep(1)
    pyautogui.moveTo(parte)
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
    pyautogui.moveTo(novo)
    pyautogui.click()
    pyautogui.click()

    time.sleep(0.5)

    # Rolar tela
    pyautogui.scroll(-300)
