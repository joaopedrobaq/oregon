import sys
import pyperclip
import pyautogui
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QInputDialog, QMessageBox
from processo import selectProcesso

app = QApplication(sys.argv)
window = QWidget()

# Cria os botões
button1 = QPushButton("Abrir Processo")
button2 = QPushButton("Pegar Coordenadas")
button3 = QPushButton("Eliminar Linhas Extras")


# Função do Botão de Abrir Processo
def abrir_processo():
    text, ok = QInputDialog.getText(window, "Caixa de texto", "Digite algo:")
    if ok:
        # Realizar ações com número do processo
        selectProcesso(0, text)
        print(f"Texto digitado: {text}")


button1.clicked.connect(abrir_processo)


# Função do Botão de Pegar Coordenadas
def pegar_coordenadas():
    time.sleep(2)
    x, y = pyautogui.position()

    string = f"({x}, {y})"
    print(string)
    pyperclip.copy(string)

    # msg_box = QMessageBox()

    # # Define o título e o texto do diálogo
    # msg_box.setWindowTitle('Coordenadas')
    # msg_box.setText(f'X: {x} Y: {y}')
    # msg_box.exec_()


button2.clicked.connect(pegar_coordenadas)

# Cria o gerenciador de layout e adiciona os botões
layout = QHBoxLayout()
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)

# Define o gerenciador de layout como o gerenciador de layout da janela principal
window.setLayout(layout)
window.setWindowTitle("Oregon")

window.show()
sys.exit(app.exec_())
