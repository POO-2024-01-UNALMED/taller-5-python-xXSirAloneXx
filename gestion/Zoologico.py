class Zoologico:
    _zonas = []

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nNombre):
        self._nombre = nNombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, nUbicacion):
        self._ubicacion = nUbicacion

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    @classmethod
    def setZona(cls, zonas):
        cls._zonas = zonas

    def cantidadTitalAnimales(self):
        cantidadA = 0
        for zona in self._zonas:
            cantidadA += zona.cantidadAnimales()
        return cantidadA
    