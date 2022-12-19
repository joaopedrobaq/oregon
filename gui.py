import sys
import pyperclip
import pyautogui
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QInputDialog, QMessageBox
from processo import selectProcesso
from lista import tratarLista, cadastrador

app = QApplication(sys.argv)
window = QWidget()

pc = 3

# Cria os botões
button1 = QPushButton("Abrir Processo")
button2 = QPushButton("Pegar Coordenadas")
button3 = QPushButton("Inserir Lista")
button4 = QPushButton("Cadastrar")


# Função do Botão de Abrir Processo
def abrir_processo():
    text, ok = QInputDialog.getText(window, "Caixa de texto", "Digite algo:")
    if ok:
        # Realizar ações com número do processo
        selectProcesso(pc, text)
        print(f"Texto digitado: {text}")


button1.clicked.connect(abrir_processo)


# Função do Botão de Pegar Coordenadas
def pegar_coordenadas():
    time.sleep(2)
    x, y = pyautogui.position()

    string = f"({x}, {y})"
    print(string)
    pyperclip.copy(string)

    msg_box = QMessageBox()

    # Define o título e o texto do diálogo
    msg_box.setWindowTitle('Coordenadas')
    msg_box.setText(f'X: {x} Y: {y}')
    msg_box.exec_()


button2.clicked.connect(pegar_coordenadas)


def inserirLista():
    # Abre o diálogo de entrada e obtém o texto digitado pelo usuário
    text, ok = QInputDialog.getMultiLineText(None,
                                             'Inserção de Lista',
                                             'Lista de Nomes:')

    if ok:
        # Se o usuário clicar em "OK", exibe o texto digitado
        global nomes
        nomes = tratarLista(text)
        print(nomes)


button3.clicked.connect(inserirLista)


def cadastrarLista():
    cadastrador(pc, nomes)


button4.clicked.connect(cadastrarLista)

# Cria o gerenciador de layout e adiciona os botões
layout = QHBoxLayout()
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)

# Define o gerenciador de layout como o gerenciador de layout da janela principal
window.setLayout(layout)
window.setWindowTitle("Oregon")

window.show()
sys.exit(app.exec_())
