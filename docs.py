import json
import pyautogui
import pyperclip

with open('processos.json', 'r') as f:
    data = json.load(f)

i = 39
string = ""
for item in data:
    string += f"\n\n{i} - {item['processo']}\n\n"
    n = 1
    for nome in item['nomes']:
        string += f"{n}) {nome}\n"
        n += 1
    i += 1
pyperclip.copy(string)
#pyautogui.hotkey('ctrl', 'v')