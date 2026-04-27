import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QVBoxLayout, QHBoxLayout, QWidget, 
    QLineEdit, QLabel
)
from PyQt6.QtCore import Qt 

# subclasse de QMainWindow para criar toda nossa janela e seus componente
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # título da janela + tamanho da janela
        self.setWindowTitle("Conversor Inteligente")
        self.setMinimumSize(400, 180)

        # 1. Componentes

        # input + placeholder
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Digite algo...")
        
        # botões
        self.button_upper = QPushButton("MAIÚSCULAS") 
        self.button_lower = QPushButton("minúsculas") 
        
        # botões começam desabilitados
        self.button_upper.setEnabled(False)
        self.button_lower.setEnabled(False)

        # texto + centralização do texto
        self.result_label = QLabel("Aguardando entrada...")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # 2. Layouts

        # cria uma fila vertical, onde, cada componente adiciona ficará um embaixo do outro
        main_layout = QVBoxLayout()
        # cria uma fila horizontal, onde, cada componente adiciona ficará um do lado do outro
        button_layout = QHBoxLayout()

        # coloca o botão maiúsculo na fila horizontal (a esquerda por ser o primeiro)
        button_layout.addWidget(self.button_upper)
        # coloca o botão minúsculo na fila horizontal (ao lado do botão acima)
        button_layout.addWidget(self.button_lower)

        # coloca o input na fila vertical (no topo)
        main_layout.addWidget(self.input_text)
        # coloca a linha com os botões na segunda posição da linha vertical
        main_layout.addLayout(button_layout)
        # coloca o texto do resulto na última posição da linha vertical
        main_layout.addWidget(self.result_label)

        # cria um espaço vazio
        container = QWidget()
        # coloca a linha vertical (com a horizontal dentro) no espaço vazio
        container.setLayout(main_layout)
        # coloca o espaço vazio (com as linhas) para ocupar toda a tela
        self.setCentralWidget(container)

        # conectando botões à suas funções
        self.button_upper.clicked.connect(self.to_upper)
        self.button_lower.clicked.connect(self.to_lower)
        
        # conecta input à sua função de verificação se o usuário digitou algo
        self.input_text.textChanged.connect(self.toggle_buttons)

    # verifica se o usuário digitou algo no input para liberar os botões
    def toggle_buttons(self):
        # verifica se o input está vazio ou só com espaços (True)
        esta_vazio = len(self.input_text.text().strip()) == 0
        
        # se esta_vazio for True o enable fica False, e vice-versa
        self.button_upper.setEnabled(not esta_vazio)
        self.button_lower.setEnabled(not esta_vazio)
        
        # se esta_vazio for True o texto diz isso abaixo
        if esta_vazio:
            self.result_label.setText("Aguardando entrada...")

    def to_upper(self):
        self.result_label.setText(self.input_text.text().upper())

    def to_lower(self):
        self.result_label.setText(self.input_text.text().lower())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())