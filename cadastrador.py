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
string = """
7561 ROSANGELA CHAVES SOUTO VIANA 
7562 ROSANGELA CRISTINA PEROBA DA SILVA 
7563 ROSANGELA FERREIRA FIGUEIREDO 
7564 ROSANGELA GONZAGA NOGUEIRA 
7565 ROSANGELA LEMOS MAIA DE ABREU 
7566 ROSANGELA MALLMANN ALMEIDA 
7567 ROSANGELA NASCIMENTO NOBRE 
7568 ROSANGELA PEREIRA S OLIVEIRA 
7569 ROSANGELA REZENDE DE OLIVEIRA 
7570 ROSANGELA RODRIGUES SILVA 
7571 ROSANGELA SILVA BITTENCOURT 
7572 ROSANGELA SIMOES PALAVIZINI 
7573 ROSANGELA VIEIRA DE ARAUJO 
7574 ROSANY FERNANDES GARCIA 
7575 ROSE MARY BRAGA DE LIMA 
7576 ROSE MARY MAGALHAES PRATES 
7577 ROSE MARY ROZO DAVID 
7578 ROSEANE QUEIROZ MONTEIRO 
7579 ROSEANE VILAS BOAS PEREIRA 
7580 ROSELENA DE AMORIM VIANA

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
