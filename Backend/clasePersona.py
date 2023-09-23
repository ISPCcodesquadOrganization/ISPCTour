class Persona:


    def __init__(self):

        self.username = input("Ingrese un nombre de usuario: ")
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.dirección = input("Ingrese su dirección: ")
        self.email = input("Ingrese su email: ")
        self.contraseña = input("Ingrese una contraseña: ")
        
        print("Se ha registrado correctamente")

    
    def registrarse(self):
        print(f'El usuario ingresado {self.username} se ha registrado correctamente.')


    def verificar(self, contraseña_ingresada):
        return self.contraseña == contraseña_ingresada
    

    def acceder(self):

        username = input("Ingresar nombre de usuario: ")
        contraseña = input("Ingresar contraseña: ")

        if self.username == username and self.verificar(contraseña):
            print(f"Bienvenido, {self.nombre} {self.apellido}!")
        else:
            print("Nombre de usuario o contraseña incorrecta")

    

    def cambiar_contraseña(self):

        contraseña_actual = input("Ingrese su contraseña actual: ")

        if self.verificar(contraseña_actual):
            nueva_contraseña = input("Ingrese una nueva contraseña: ")
            self.contraseña = nueva_contraseña
            print("Contraseña cambiada exitosamente")
        else:
            print("No se puede cambiar contraseña")



usuario1 = Persona()
usuario1.registrarse()

usuario1.acceder()

usuario1.cambiar_contraseña()

usuario1.acceder()


