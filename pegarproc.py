import pyautogui
import pyperclip
import json 
import time 
import re

string = ''

time.sleep(2)

for i in range (0, 15):
  pyautogui.hotkey('ctrl', 'c')
  # extrair apenas o numero do processo
  regex = "\d{7}-\d{2}.\d{4}.\d{1}.\d{2}.\d{4}"

  match = re.search(regex, pyperclip.paste())
  if match:
    string += match.group() + "\n"
    print(f"{match.group()}")
  # seta para baixo e reinicio
  pyautogui.press('down')
  time.sleep(1)

pyperclip.copy(string)
#print(string)