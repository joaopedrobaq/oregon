import pyautogui
import time
import pyperclip
import json
from coords import coords

pc = 0

processo = "0000714-71.2022.5.05.0018"

anotacoes = '''
AÇÃO 
DE EXECUÇÃO AUTÔNOMA PROVISÓRIA, do Título Judicial decorrente 
do Processo nº 0001164.33.2012.5.05.0028
5901 MARIA DE FATIMA PESSOA 
5902 MARIA DE FATIMA QUEIROZ MARQUES 
5903 MARIA DE FATIMA SOUZA AMARAL 
5904 MARIA DE FATIMA SOUZA F SANTOS 
5905 MARIA DE FATIMA TEIXEIRA 
5906 MARIA DE LOURDES BERNARDO 
5907 MARIA DE LOURDES CORREIA 
5908 MARIA DE LOURDES LOPES SILVA 
5909 MARIA DELZIRA BARRETO 
5910 MARIA DENILDA DE SOUZA CORDEIRO 
5911 MARIA DILMA MAGALHAES OLIVEIRA 
5912 MARIA DILMA SANTOS ANDRADE 
5913 MARIA DIVINA COSTA RIBEIRO 
5914 MARIA DO ALIVIO LIMA DA SILVA 
5915 MARIA DO CARMO ARAUJO LOPES 
5916 MARIA DO CARMO CARVALHO DIAS 
5917 MARIA DO CARMO DE A ESPINHEIRA 
5918 MARIA DO CARMO LESSA P BRANDAO 
5919 MARIA DO CARMO SANTOS PIMENTEL 
5920 MARIA DO PERPETUO SOCORRO V BARBOSA
'''

# Pegar do JSON
with open('processos.json', 'r') as f:
    data = json.load(f)

i = 1
for item in data:
  print(f'{i}) {item["processo"]}')
  i += 1

i = int(input("Qual processo você quer?")) - 1
 
processo = data[i]['processo']

anotacoes = f'''AÇÃO DE EXECUÇÃO AUTÔNOMA PROVISÓRIA, do Título Judicial decorrente do Processo nº {data[i]['origem']} 
'''
n = 1
for nome in data[i]['nomes']:
  anotacoes += f'''
{n}) {nome} '''
  n += 1

# CADASTROS 
pyautogui.moveTo(coords[pc]['cadastros'])
pyautogui.click()
# NOVO PROCESSO 
time.sleep(0.5)
pyautogui.moveTo(coords[pc]['novoprocesso']['cadastroProcesso'])
pyautogui.click()

# NUMERO PROCESSO
time.sleep(2)
pyautogui.moveTo(coords[pc]['novoprocesso']['numero'])
pyautogui.click()
pyperclip.copy(processo)
pyautogui.hotkey('ctrl', 'v')

# NATUREZA - TRABALHISTA
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("T", 0.1)
time.sleep(1)
pyautogui.press("enter")

# AÇÃO - TRABALHISTA
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("T", 0.1)
time.sleep(1)
pyautogui.press("enter")

# ADVOGADO - PITANGA
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("Pedro C", 0.1)
pyautogui.press("enter")

# PROCEDIMENTO - ORDINARIO
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("Ordin", 0.1)
pyautogui.press("enter")

# COLETIVO CHECK
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("space")

# VALOR DA CAUSA - 70K
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("70.000,00")

# ANOTAÇÕES
pyautogui.press("tab")
pyperclip.copy(anotacoes)
pyautogui.hotkey('ctrl', 'v')

# CRIAR
pyautogui.moveTo(coords[pc]['novoprocesso']['criar'])
pyautogui.click()

# NOVAS PARTES
time.sleep(1)
pyautogui.moveTo(coords[pc]['novoprocesso']['novaParte'])
pyautogui.click()
pyautogui.click()
time.sleep(0.5)
pyautogui.click()
pyautogui.click()

# PARTE SINDICATO - AUTOR
pyautogui.moveTo(coords[pc]['novoprocesso']['primeiraParte'])
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(coords[pc]['busca'])
pyautogui.click()
pyautogui.write("Sindicato dos banc")
pyautogui.press("enter")

time.sleep(4)

# Pegar primeiro resultado
pyautogui.moveTo(coords[pc]['primeiro'])
pyautogui.click()
pyautogui.click()
time.sleep(0.5)
pyautogui.press("tab")
pyperclip.copy("Parte")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("tab")
pyautogui.hotkey('shift', 'tab')
pyperclip.copy("Parte")
pyautogui.hotkey('ctrl', 'v')
#pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("Autor")
# pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("space")
pyautogui.press("tab")

# PARTE BANCO - RÉU
pyautogui.moveTo(coords[pc]['novoprocesso']['segundaParte'])
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(coords[pc]['busca'])
pyautogui.click()
pyautogui.write("Banco do Brasil")
pyautogui.press("enter")

time.sleep(4)

# Pegar primeiro resultado
pyautogui.moveTo(coords[pc]['primeiro'])
pyautogui.click()
pyautogui.click()
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("Parte")
# pyautogui.press("enter")
pyautogui.press("tab")
pyperclip.copy("Réu")
pyautogui.hotkey('ctrl', 'v')
# pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("space")