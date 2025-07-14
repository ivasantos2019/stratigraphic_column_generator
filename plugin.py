from qgis.PyQt.QtWidgets import QAction, QDockWidget
from qgis.PyQt.QtCore import Qt
from qgis.utils import iface
from .geo3d_viewer import Geo3DViewer

class Geo3DViewPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.dock = None
        self.action = None
        self.viewer = None

    def initGui(self):
        self.action = QAction("3DGeoView", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("&3DGeoView", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        if self.dock:
            self.iface.removeDockWidget(self.dock)
            self.dock = None
        if self.action:
            self.iface.removePluginMenu("&3DGeoView", self.action)
            self.iface.removeToolBarIcon(self.action)


