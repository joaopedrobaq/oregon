import re
import time
import pyautogui
import keyboard
# Regex para pegar apenas os nomes

# String para extrair os nomes
string = """Processo nº 0001173.16.2012.5.05.0021

1) VERA LUCIA SANTARÉM TELES 
2) VERA LUCIA SOUSA PEREIRA 
3) VERENA MARQUES PINHEIRO LEAL 
4) VE RIVAL ARRUDA SOARES CRUZ 
5) VICENTE BRANDAO LOPES FILHO 
6) VICENTE JORGE PEREIRA MENDES 
7) VICENTE SANTANA BARREIRA 
8) VICTOR SILVA DOS SANTOS 
9) VILMA TAVARES DA SILVA BRITO 
10) VINÍCIUS RENAN SOUZA ABREU 
11) VINÍCIUS TEIXEIRA MOURA SANTOS 
12) VITOR ALESANDRO DE A CORDEIRO 
13) VITOR BRITO QUEIROZ 
14) VITOR SANTOS OLIVEIRA 
15) VIVALDO CARMO DE SOUZA 
16) VIVIAN MACHADO BARBOSA 
17) WAGNER FERREIRA MATOS 
18) WAGNER REBOUCAS ALMEIDA 
19) WALDENIR SIDNEY FAGUNDES BRITO 
20) WALDIR MOREIRA DIOGO
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
    for i in range (inicio, len(nomes)):
        # Fazer o que quer com cada nome
        print(f"{i+1}) {nomes[i]}")

        # Clicar no ...
        pyautogui.moveTo(310, 520)
        pyautogui.click()

        time.sleep(2)

        # Clicar na busca
        pyautogui.moveTo(846, 215)
        pyautogui.click()
        pyautogui.write(nomes[i])
        pyautogui.press("enter")

        time.sleep(4)

        # Pegar primeiro resultado
        pyautogui.moveTo(430, 245)
        pyautogui.click()
        pyautogui.click()

        # Colocar como Parte
        time.sleep(1)
        pyautogui.moveTo(460,520)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.move(0,50)
        pyautogui.click()

        #Colocar como Autor
        time.sleep(0.5)
        pyautogui.move(130,-50)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.move(0,-320)
        pyautogui.click()

        # Rolar tela
        pyautogui.scroll(-300)

        # Abrir mais um
        pyautogui.moveTo(310,600)
        pyautogui.click()
        pyautogui.click()
        
        time.sleep(0.5)

        # Rolar tela
        pyautogui.scroll(-300)
