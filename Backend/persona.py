import os
import time
import mysql.connector
from mysql_conexion import conectar_bd, cerrar_bd

class Persona:

    def __init__(self):
        self.username = self.verificarDisponibilidad()
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.direccion = input("Ingrese su dirección: ")
        self.email = input("Ingrese su email: ")
        self.telefono = input("Ingrese su numero de telefono: ")
        self.contraseña = input("Ingrese una contraseña: ")

        try:
            # Conectar a la base de datos
            conexion = conectar_bd()

            # Verificar la conexión
            if conexion:
                cursor = conexion.cursor()

                sentencia = "INSERT INTO personas (nombre,apellido, email, nombreUsuario, Telefono, direccionUsuario, contraseña) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.nombre,self.apellido, self.email, self.username, self.telefono, self.direccion, self.contraseña)
                cursor.execute(sentencia)
                conexion.commit()

                sentencia2 = "SELECT idUsuarios FROM personas WHERE nombreUsuario = '{}'".format(self.username)
                cursor.execute(sentencia2)
                usuario_provisorio = cursor.fetchone()
                numero_entero = int(usuario_provisorio[0])
                rol_usuario = 3

                sentencia3 = "INSERT INTO `personas_has_tipo de rol` (Personas_idUsuarios, fk_Tipo_de_rol)  VALUES ('{}', '{}')".format(numero_entero, rol_usuario)
                cursor.execute(sentencia3)
                conexion.commit()

                cursor.close()
                cerrar_bd(conexion)

            else:
                print("No se pudo conectar a la base de datos.")

            cerrar_bd(conexion)

        except mysql.connector.Error as e:
            print("Error:", e)

        print("Se ha registrado correctamente!")

    def verificarDisponibilidad(self):
        nombreUsuario = input("Ingrese un nombre de usuario: ")
        try:
            conexion = conectar_bd()

            # Verificar la conexión
            if conexion:
                cursor = conexion.cursor()

                # Consulta SQL para verificar si el usuario existe en la tabla Personas
                consulta = "SELECT COUNT(*) FROM personas WHERE nombreUsuario = %s"
                cursor.execute(consulta, (nombreUsuario,))
                resultado = cursor.fetchone()

                if resultado[0] > 0:
                    print('El usuario elegido no se encuentra disponible')
                    time.sleep(1)
                    os.system('cls')
                    return self.verificarDisponibilidad()
                else:
                    print('Usuario disponible')
                    return nombreUsuario  # El usuario no existe

            else:
                print("No se pudo conectar a la base de datos.")

            cerrar_bd(conexion)

        except mysql.connector.Error as e:
            print("Error:", e)

    
    def verificar_usuario(self):
        try:
            # Conectar a la base de datos
            conexion = conectar_bd()

            # Verificar la conexión
            if conexion:
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
                    
                        return nombre_usuario
                    else:
                        print('Usuario o contraseña incorrectos')
                        return False  # El usuario no existe
                    
                else:
                    print('Usuario o contraseña incorrectos')
                    return False  # El usuario no existe
                
            else:
                print("No se pudo conectar a la base de datos.")

            cerrar_bd(conexion)

        except mysql.connector.Error as e:
            print("Error:", e)

    def verificar_usuario1(self):
        try:
            # Conectar a la base de datos
            conexion = conectar_bd()

            # Verificar la conexión
            if conexion:
                cursor = conexion.cursor()

                nombre_usuario = input('Ingrese su nombre de usuario: ')
                contraseña = input('Ingrese su contraseña: ')

                # Consulta SQL para verificar si el usuario existe en la tabla Personas
                consulta = "SELECT idUsuarios FROM personas WHERE nombreUsuario = %s AND contraseña = %s"
                cursor.execute(consulta, (nombre_usuario, contraseña))
                resultado = cursor.fetchone()

                # Comprobar si el usuario existe y la contraseña es correcta
                if resultado:
                    # Devuelve el ID de usuario si la verificación es exitosa
                    return resultado[0]
                else:
                    print('Usuario o contraseña incorrectos')
                    return None  # Retorna None si la verificación falla

            else:
                print("No se pudo conectar a la base de datos.")

            cerrar_bd(conexion)

        except mysql.connector.Error as e:
            print("Error:", e)



    


