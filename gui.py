import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Oregon")
        self.UIComponents()
        self.resize(500, 500)

    def UIComponents(self):
        # cria cinco botões
        button1 = QPushButton("Encontrar Processo", self)
        button2 = QPushButton("Cadastrar Lista", self)
        button3 = QPushButton("Adicionar Nomes Processo", self)
        button4 = QPushButton("Adicionar Nome Novo", self)
        button5 = QPushButton("Eliminar Linhas e Salvar", self)

        # posiciona os botões na tela
        button1.move(50, 50)
        button2.move(50, 100)
        button3.move(50, 150)
        button4.move(50, 200)
        button5.move(50, 250)

        # aplica o estilo CSS aos botões
        button1.setStyleSheet(
            "color: black; background-color: lightblue; font-size: 20px;")
        button2.setStyleSheet(
            "color: black; background-color: lightblue; font-size: 20px;")
        button3.setStyleSheet(
            "color: black; background-color: lightblue; font-size: 20px;")
        button4.setStyleSheet(
            "color: black; background-color: lightblue; font-size: 20px;")
        button5.setStyleSheet(
            "color: black; background-color: lightblue; font-size: 20px;")

        # Ajustar tamanho dos botões
        button1.adjustSize()
        button2.adjustSize()
        button3.adjustSize()
        button4.adjustSize()
        button5.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
