from .GISCopilot import GISCopilot

def classFactory(iface):
    return GISCopilot(iface)