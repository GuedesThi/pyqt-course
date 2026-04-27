from PyQt6.QtWidgets import (
    QApplication,   # configurações do programa
    QMainWindow,    # tela principal com suportes
    QWidget,        # espaço vazio
    QVBoxLayout,    # flexbox vertical
    QHBoxLayout,    # flexbox horizontal
    QLineEdit,      # input
    QPushButton,    # botão
    QLabel,         # widget para exibir textos ou imagens
    QStackedWidget, # espaço que armazena várias páginas e mostra uma por vez
    QFrame          # widget com moldura para criar "cards" ou divisores visuais
)

from PyQt6.QtCore import Qt
import sys 
from engine import StatsEngine
from styles import STYLE_SHEET

# tela usada para cada conceito de estatística
class CalcPage(QWidget):
    # informações da página que mudaram de acordo com o conceito
    def __init__(self, title, concept, formula_text, calc_fn):
        # pega atributos e métodos de QWidget
        super().__init__()

        # flexbox vertical
        layout = QVBoxLayout(self)
        # espaços da borda da página
        layout.setContentsMargins(50, 50, 50, 50)
        # espaço entre os componentes da página
        layout.setSpacing(25)
        # alinha os componentes no topo
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # widget para exibir textos ou imagens, usei para criar o cabeçalho da página
        lbl_title = QLabel(title)
        # cria um ID que é o mesmo usado no nosso código CSS
        lbl_title.setObjectName("Title")
        
        # widget para exibir textos ou imagens, usei para criar o sub-título da página
        lbl_concept = QLabel(concept)
        # cria um ID que é o mesmo usado no nosso código CSS
        lbl_concept.setObjectName("Subtitle")
        # permite que o texto quebre linhas automaticamente
        lbl_concept.setWordWrap(True)

        # widget para exibir textos ou imagens, usei para mostrar a fórmula
        lbl_form = QLabel(f"Fórmula Acadêmica: {formula_text}")
        # cria um ID que é o mesmo usado no nosso código CSS
        lbl_form.setObjectName("Formula")

        # input para os valores das operações
        self.input_vals = QLineEdit()
        # placeholder
        self.input_vals.setPlaceholderText("Exemplo: 12, 45, 33.5, 10")

        # botão para enviar os valores
        btn_calc = QPushButton("Processar Dados e Mostrar Passos")
        # cria um ID que é o mesmo usado no nosso código CSS
        btn_calc.setObjectName("ActionBtn")
        # muda o símbolo do mouse para a mãozinha ao passar por cima
        btn_calc.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # widget com moldura para criar "cards" ou divisores visuais, usei para área dos resultado
        self.result_box = QFrame()
        # cria um ID que é o mesmo usado no nosso código CSS
        self.result_box.setObjectName("ResultCard")
        # começa invisível
        self.result_box.hide()
        
        # coloca a área do resultados num flexbox vertical
        res_layout = QVBoxLayout(self.result_box)
        # widget para exibir textos ou imagens, usei para colocar o passo a passo
        self.lbl_steps = QLabel("")
        # fiz sua estilização aqui mesmo
        self.lbl_steps.setStyleSheet("color: #10b981; font-family: 'Consolas'; font-size: 14px; line-height: 150%;")
        # adicionei o espaço com o passo a passo no flexbox vertical com a área do resultados
        res_layout.addWidget(self.lbl_steps)

        # conecto o botão de enviar os valores com o método run_calc()
        btn_calc.clicked.connect(lambda: self.run_calc(calc_fn))

        # adicionei o cabeçalho da página no flexbox vertical
        layout.addWidget(lbl_title)
        # adicionei o sub-título da página no flexbox vertical
        layout.addWidget(lbl_concept)
        # adicionei o texto da fórmula no flexbox vertical
        layout.addWidget(lbl_form)

        # widget para exibir textos ou imagens, usei para título do input de valores
        lbl_input_title = QLabel("DADOS DE ENTRADA:")
        # cria um ID que é o mesmo usado no nosso código CSS
        lbl_input_title.setObjectName("Subtitle")
        # adiciona um espaço nesse ponto
        layout.addSpacing(10)
        # adicionei o título do input de valores no flexbox vertical
        layout.addWidget(lbl_input_title)
        # adicionei o input para os valores das operações no flexbox vertical
        layout.addWidget(self.input_vals)
        # adicionei o botão para enviar os valores no flexbox vertical
        layout.addWidget(btn_calc)
        # adicionei a área dos resultado no flexbox vertical
        layout.addWidget(self.result_box)

    # método conectado ao botão de enviar os valores
    # calc_fn é um dos métodos de StatsEngine para operações de estatística
    def run_calc(self, calc_fn):
        # usa StatsEngine para tratar e pegar os valores digitados
        data = StatsEngine.get_data(self.input_vals.text())
        # se os dados forem inválidos
        if data is None or len(data) == 0:
            # adiciona no texto do passo a passo esse aviso
            self.lbl_steps.setText("❌ ERRO: Certifique-se de usar números separados por vírgula.")
            # mostra a área dos resultado com o aviso acima
            self.result_box.show()
            return
        
        # resultados do método específico de StatsEngine
        res, form, steps = calc_fn(data)
        # adiciona no texto do passo a passo esse resultado
        self.lbl_steps.setText(f"✅ RESULTADO FINAL: {res:.4f}\n\nMEMORIAL DE CÁLCULO:\n{steps}")
        # mostra a área dos resultado com o resultado acima
        self.result_box.show()

# tela principal de dashboard
class DashboardScreen(QWidget):
    def __init__(self, parent):
        # pega atributos e métodos de QWidget
        super().__init__()
        # referência para a MainWindow (pai)
        self.parent = parent
        # flexbox horizontal
        main_layout = QHBoxLayout(self)
        # espaços da borda da página
        main_layout.setContentsMargins(0, 0, 0, 0)
        # espaço entre os componentes da página
        main_layout.setSpacing(0)

        # widget com moldura para criar cards ou divisores visuais, usei para criar o espaço do sidebar
        sidebar = QFrame()
        # cria um ID que é o mesmo usado no nosso código CSS
        sidebar.setObjectName("Sidebar")
        # largura fixa da lateral
        sidebar.setFixedWidth(260)
        # flexbox vertical com o espaço do sidebar
        side_layout = QVBoxLayout(sidebar)
        # espaços da borda da página
        side_layout.setContentsMargins(15, 30, 15, 30)
        
        brand = QLabel("📊 STATS.LAB")
        brand.setStyleSheet("color: #3b82f6; font-weight: 900; font-size: 22px; margin-bottom: 30px;")
        side_layout.addWidget(brand)

        # Navegação
        options = [
            ("🏠 Início", 0),
            ("📈 Média Aritmética", 1),
            ("📏 Variância", 2),
            ("📉 Desvio Padrão", 3)
        ]

        for text, index in options:
            btn = QPushButton(text)
            btn.setObjectName("MenuBtn")
            btn.setCheckable(True)
            btn.setAutoExclusive(True)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda _, i=index: self.content_stack.setCurrentIndex(i))
            side_layout.addWidget(btn)
            if index == 0: btn.setChecked(True)
        
        side_layout.addStretch()

        # 2. ÁREA DE CONTEÚDO
        content_area = QWidget()
        content_layout = QVBoxLayout(content_area)
        content_layout.setContentsMargins(0, 0, 0, 0)

        self.content_stack = QStackedWidget()
        
        # PÁGINA HOME
        home_pg = QWidget()
        h_lay = QVBoxLayout(home_pg)
        h_lay.setContentsMargins(60, 60, 60, 60)
        
        h_title = QLabel("Laboratório Estatístico v1.0")
        h_title.setObjectName("Title")
        h_subtitle = QLabel("Utilize o menu lateral para selecionar uma operação matemática.\nInsira seus conjuntos de dados e aprenda o passo a passo da resolução.")
        h_subtitle.setObjectName("Subtitle")
        
        h_lay.addWidget(h_title)
        h_lay.addWidget(h_subtitle)
        h_lay.addStretch()

        # Adicionando Páginas ao Stack
        self.content_stack.addWidget(home_pg) # Index 0
        self.content_stack.addWidget(CalcPage("Média Aritmética", "Representa o ponto de equilíbrio de um conjunto de dados.", "μ = Σx/n", StatsEngine.calc_mean))
        self.content_stack.addWidget(CalcPage("Variância Amostral", "Mede quão distantes os valores estão da média.", "s² = Σ(x-μ)²/(n-1)", StatsEngine.calc_variance))
        self.content_stack.addWidget(CalcPage("Desvio Padrão", "A raiz quadrada da variância, retornando à unidade original dos dados.", "σ = √s²", StatsEngine.calc_std_dev))

        content_layout.addWidget(self.content_stack)
        
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content_area)

# tela principal
class MainWindow(QMainWindow):
    def __init__(self):
        # pega atributos e métodos de QMainWindow
        super().__init__()
        # título da tela
        self.setWindowTitle("Simulador Acadêmico de Estatística")
        # tamanho da tela
        self.resize(1200, 800)
        # CSS da tela
        self.setStyleSheet(STYLE_SHEET)
        
        # espaço que armazena várias páginas e mostra uma por vez
        self.stack = QStackedWidget()
        # coloca esse espaço para tomar toda a tela principal
        self.setCentralWidget(self.stack)

        # tela de dashboard
        self.dash = DashboardScreen(self)
        # botão a tela de dashboard no espaço que toma toda a tela principal
        self.stack.addWidget(self.dash)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    win = MainWindow()
    win.show()
    sys.exit(app.exec())