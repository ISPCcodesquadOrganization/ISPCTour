class Paquetes:
    
    def __init__(self, fechaInicio, fechaFin, destino, tipoTransporte, cantidadViajantes):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.destino = destino
        self.tipoTransporte = tipoTransporte
        self.cantidadViajantes = cantidadViajantes
        
    def getFechaInicio(self):
        return self.fechaInicio
    
    def setFechaInicio(self, fechaInicio):
        self.fechaInicio = fechaInicio
    
    def getFechaFin(self):
        return self.fechaFin
    
    def setFechaFin(self, fechaFin):
        self.fechaFin = fechaFin

    def getDestino(self):
        return self.destino
    
    def setDestino(self, destino):
        self.destino = destino

    def getTipoTransporte(self):
        return self.tipoTransporte
    
    def setTipoTransporte(self, tipoTransporte):
        self.tipoTransporte = tipoTransporte

    def getCantidadViajantes(self):
        return self.cantidadViajantes
    
    def setCantidadViajantes(self, cantidadViajantes):
        self.cantidadViajantes = cantidadViajantes
