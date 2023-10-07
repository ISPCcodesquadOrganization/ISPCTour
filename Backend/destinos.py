class Destinos:
    
    def __init__(self,destino,descripcion,precio):
        self.destino = destino
        self.descripcion = descripcion
        self.precio = precio
        
    def getDestino(self):
        return self.destino
    
    def setDestino(self,destino):
        self.destino = destino
        
    def getDescripcion(self):
        return self.descripcion
    
    def setDescripcion(self,descripcion):
        self.descripcion = descripcion
        
    def getPrecio(self):
        return self.precio
    
    def setPrecio(self,precio):
        self.precio = precio
    
        
        