import mysql.connector

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

    def verificar_usuario(self):
        try:
            # Conectar a la base de datos
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="ispc_tour"
            )

            # Verificar la conexión
            if conexion.is_connected():
                cursor = conexion.cursor()

                nombre_usuario = input('Ingrese su nombre de usuario: ')
                contraseña = input('Ingrese su contraseña: ')

                # Consulta SQL para verificar si el usuario existe en la tabla Personas
                consulta = "SELECT COUNT(*) FROM personas WHERE nombreUsuario = '{}'".format(nombre_usuario)

                cursor.execute(consulta)
                resultado = cursor.fetchone()

                # Comprobar si el usuario existe
                if resultado[0] > 0:
                    #print('existe')
                    consulta_contraseña = "SELECT contraseña FROM personas WHERE nombreUsuario = '{}'".format(nombre_usuario)
                    cursor.execute(consulta_contraseña)
                    resultado_contraseña = cursor.fetchone()

                    if resultado_contraseña[0] == contraseña:
                        #print('ta funcionando')
                        return nombre_usuario
                    else:
                        print('Usuario o contraseña incorrectos')
                        return False  # El usuario no existe
                    
                else:
                    print('Usuario o contraseña incorrectos')
                    return False  # El usuario no existe
                

                cursor.close()
                conexion.close()
            else:
                print("No se pudo conectar a la base de datos.")

        except mysql.connector.Error as e:
            print("Error:", e)

    #def prueba():
     #   print('Funciona')