from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QPushButton, QLabel
from .llm_interface import consultar_modelo_local

class GISCopilotDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GISCopilot")
        self.setMinimumWidth(500)

        self.layout = QVBoxLayout()

        self.instrucao = QTextEdit()
        self.instrucao.setPlaceholderText("Descreva o que deseja fazer no QGIS...")

        self.gerar_btn = QPushButton("Gerar Código")
        self.executar_btn = QPushButton("Executar Código")

        self.codigo_output = QTextEdit()
        self.codigo_output.setReadOnly(True)

        self.layout.addWidget(QLabel("Instrução em linguagem natural:"))
        self.layout.addWidget(self.instrucao)
        self.layout.addWidget(self.gerar_btn)
        self.layout.addWidget(QLabel("Código PyQGIS gerado:"))
        self.layout.addWidget(self.codigo_output)
        self.layout.addWidget(self.executar_btn)

        self.setLayout(self.layout)

        # 👇 Aqui está a conexão do botão com a função
        self.gerar_btn.clicked.connect(self.gerar_codigo)

    def gerar_codigo(self):
        prompt = self.instrucao.toPlainText().strip()
        if prompt:
            codigo = consultar_modelo_local(prompt)
            self.codigo_output.setPlainText(codigo)
        else:
            self.codigo_output.setPlainText("[Nenhuma instrução fornecida]")
