class Hoteles:
    
    def __init__(self, nombreHotel, direccionHotel, telefono):
        self.nombreHotel = nombreHotel
        self.direccionHotel = direccionHotel
        self.telefono = telefono
        
    def getNombreHotel(self):
        return self.nombreHotel
    
    def setNombreHotel(self, nombreHotel):
        self.nombreHotel = nombreHotel
    
    def getDireccionHotel(self):
        return self.direccionHotel
    
    def setDireccionHotel(self, direccionHotel):
        self.direccionHotel = direccionHotel
    
    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self, telefono):
        self.telefono = telefono
