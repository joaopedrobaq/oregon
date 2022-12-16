import re
import time
import pyautogui
import keyboard
import pyperclip

#Editar o Valor de Acordo com o PC usado
pc = 4

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

if pc == 3:
    # Coordenadas PC Joao Porto
    abrir = (310, 490)
    busca = (1000, 280)
    primeiro = (650, 310)
    parte = (460, 490)
    novo = (300, 720)

if pc == 4:
    # Coordenadas PC Bartira
    abrir = (310, 490)
    busca = (900, 215)
    primeiro = (500, 240)
    parte = (460, 490)
    novo = (300, 600)

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
