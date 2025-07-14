from qgis.PyQt.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit,
    QMessageBox, QDialog
)
from qgis.PyQt.QtWebEngineWidgets import QWebEngineView
from qgis.PyQt.QtCore import Qt, QUrl
import requests

class Geo3DViewer(QWidget):
    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.setWindowTitle("3DGeoView - Modelos Sketchfab")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Campo de busca
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar modelo Sketchfab (ex: geologia, estrutura)")
        self.layout.addWidget(self.search_input)

        # Botão buscar
        self.search_btn = QPushButton("Buscar")
        self.search_btn.clicked.connect(self.search_models)
        self.layout.addWidget(self.search_btn)

        # Lista de resultados
        self.results_list = QListWidget()
        self.layout.addWidget(self.results_list)

        # Botão para carregar modelo
        self.load_btn = QPushButton("Visualizar modelo 3D")
        self.load_btn.clicked.connect(self.load_model)
        self.layout.addWidget(self.load_btn)

        self.models = []  # Lista para armazenar resultados da API

    def search_models(self):
        query = self.search_input.text().strip()
        if not query:
            QMessageBox.warning(self, "Aviso", "Digite um termo para busca.")
            return

        url = f"https://api.sketchfab.com/v3/search?type=models&q={query}&downloadable=true"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.models = data.get("results", [])
            self.results_list.clear()

            if not self.models:
                QMessageBox.information(self, "Resultado", "Nenhum modelo encontrado.")
                return

            for model in self.models:
                name = model.get("name", "Sem nome")
                uid = model.get("uid", "desconhecido")
                self.results_list.addItem(f"{name} [{uid}]")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha ao buscar modelos:\n{e}")

    def load_model(self):
        current_row = self.results_list.currentRow()
        if current_row == -1:
            QMessageBox.warning(self, "Aviso", "Selecione um modelo para visualizar.")
            return

        model = self.models[current_row]
        model_uid = model.get("uid")
        if not model_uid:
            QMessageBox.warning(self, "Erro", "ID do modelo inválido.")
            return

        viewer = SketchfabModelViewer(model_uid)
        viewer.exec_()


class SketchfabModelViewer(QDialog):
    def __init__(self, model_uid, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Visualizador 3D - Sketchfab")
        self.resize(900, 600)

        layout = QVBoxLayout(self)
        self.webview = QWebEngineView()
        layout.addWidget(self.webview)

        embed_url = f"https://sketchfab.com/models/{model_uid}/embed"
        self.webview.setUrl(QUrl(embed_url))
o modelo 3D para o QGIS.
        # Por enquanto, só mostra uma mensagem:
        QMessageBox.information(self, "Carregar modelo", f"Carregando modelo: {model_name}\n\n(Implementar integração 3D)")
