import re
import time
import pyautogui
import keyboard
import pyperclip
from coords import coords

#Editar o Valor de Acordo com o PC usado
# 0 = Estagiário
# 1 = Angela
# 2 = João Porto
# 3 = Bartira
pc = 0

# String para extrair os nomes
string = """
2801 FERNANDA S A L SANTOS 
2802 FERNANDA SANTOS SILVA 
2803 FERNANDA SILVA SARDEIRO 
2804 FERNANDES AVELINO DE BRITO 
2805 FERNANDO ALVES MACHADO 
2806 FERNANDO AMTONIO MANEIRA 
2807 FERNANDO ANTONIO AROUCA MACIEL 
2808 FERNANDO ANTONIO CARVALHO DE ALMEIDA 
2809 FERNANDO ANTONIO OLIVEIRA DE ANDRADE NETO 
2810 FERNANDO ANTONIO S JAMBEIRO 
2811 FERNANDO BAQUEIRO HERMIDA 
2812 FERNANDO BARROS 
2813 FERNANDO BATISTA R ALMEIDA 
2814 FERNANDO BIAGGIO FRACASSO 
2815 FERNANDO CESAR DALMOLIN 
2816 FERNANDO CESPEDES RAMOS 
2817 FERNANDO CUSTODIO DE QUEIROZ 
2818 FERNANDO DA SILVA NOBRE 
2819 FERNANDO DE ALMEIDA COELHO 
2820 FERNANDO DE CASTRO DOURADO

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
