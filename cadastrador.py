import re
import time
import pyautogui
import keyboard
import pyperclip

#Coordenadas PC Estagiário
abrir = (310, 520)
busca = (846, 215)
primeiro = (430, 245)
parte = (460, 520)
novo = (310, 600)

# Coordenadas PC Angela
abrir = (385, 490)
busca = (1000, 280)
primeiro = (650, 310)
parte = (540, 490)
novo = (300, 720)

# String para extrair os nomes
string = """Processo nº 0001173.16.2012.5.05.0021

1) ILMARA CARQUEIJA ROCHA 
2) INALDO PORTO BOMFIM JUNIOR 
3) INOCENCIO RUBEN DE ARAUJO 
4) IRANI FERREIRA LOPES ROCHA 
5) IRIS GEZA OLIVEIRA SANTOS TAVARES 
6) IRLA PEREIRA DE SOUZA 
7) ISABEL ROSEANE GUIMARAES DE OLIVEIRA 
8) ISABELA SCUCATO LOBO 
9) ISAIAS PAIXAO JUNIOR 
10) ISAIAS PEREIRA DA SILVA 
11) ISMAEL ARAUJO DE SOUZA 
12) ISMAEL PEREIRA DE SOUZA 
13) ISNAEL DE JESUS COUTINHO 
14) ISRAEL FERNANDO ALMEIDA DE SANTANA 
15) ISRAEL RIBEIRO DE SOUSA 
16) ITAIRA SOARES DE FREITAS SANTOS 
17) ITALO GIOVANNI LESSA GOMES 
18) ITALO ISAAC RODRIGUES DA SILVA 
19) ITALO JOENE TORRES MARCELINO 
20) ITAMAR GOMES MEDEIROS
"""

# Extrair os nomes e transformar em array
nomes = re.findall(r"\d+\) (.*)", string)

continuar = True

while continuar == True:
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
