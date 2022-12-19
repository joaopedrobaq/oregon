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
7501 RONALDO NASCIMENTO DOS SANTOS 
7502 RONALDO OLIVEIRA RIOS 
7503 RONALDO SAMPAIO MELO 
7504 RONALDO SILVA GOMES 
7505 RONALDO VIEIRA BORGES 
7506 RONALDO VIEIRA DE ALMEIDA 
7507 RONAN SACRAMENTO CANCISSU 
7508 RONEIDE RIBEIRO DE OLIVEIRA 
7509 RONIER SILVA OLIVEIRA FERREIRA 
7510 RONILSON FABRICIO AZEVEDO DA SILVA 
7511 RONILSON LOPES MARQUES 
7512 RONILSON PEREIRA DA SILVA 
7513 RONILSON VIEIRA DE SOUZA 
7514 RONILTON DE SENNA FERREIRA 
7515 RONNAM PEREIRA DOS SANTOS LESSA 
7516 RONNY MEIRA LIMA 
7517 RONY GLEISON SILVEIRA 
7518 ROOSEVELT BELCHIOR LIMA 
7519 ROQUE ANDREOLA 
7520 ROQUE ANTONIO SANTANA MEDEIROS

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
