def classFactory(iface):
    from .plugin import Geo3DViewPlugin
    return Geo3DViewPlugin(iface)
