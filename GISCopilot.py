# GISCopilot.py
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsMessageLog
from .GISCopilot_dialog import GISCopilotDialog

class GISCopilot:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = None
        self.dialog = None

    def initGui(self):
        self.action = QAction(QIcon(""), "GISCopilot", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&GISCopilot", self.action)

    def unload(self):
        self.iface.removePluginMenu("&GISCopilot", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        if not self.dialog:
            self.dialog = GISCopilotDialog()
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()

