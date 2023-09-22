class TipoTransporte:
    
    def __init__(self, tipoTransporte, capacidad):
        self.tipoTransporte = tipoTransporte
        self.capacidad = capacidad
        
    def getTipoTransporte(self):
        return self.tipoTransporte
    
    def setTipoTransporte(self, tipoTransporte):
        self.tipoTransporte = tipoTransporte
    
    def getCapacidad(self):
        return self.capacidad
    
    def setCapacidad(self, capacidad):
        self.capacidad = capacidad