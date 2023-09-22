class Usuario:
    def __init__(self, nombre, apellido, email, nombreUsuario, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.nombreUsuario = nombreUsuario
        self.telefono = telefono

   
    def get_nombre(self):
        return self.nombre

   
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

   
    def get_apellido(self):
        return self.apellido

    def set_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

   
    def get_email(self):
        return self.email

    def set_email(self, nuevo_email):
        self.email = nuevo_email

    def get_nombreUsuario(self):
        return self.nombreUsuario

    def set_nombreUsuario(self, nuevo_nombreUsuario):
        self.nombreUsuario = nuevo_nombreUsuario

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono


