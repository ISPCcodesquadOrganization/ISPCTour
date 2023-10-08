import mysql.connector
from mysql_conexion import conectar_bd, cerrar_bd

class Administrador:

    def verificarAdministrador(usuario):
        try:
            # Conectar a la base de datos
            conexion = conectar_bd()

            # Verificar la conexión
            if conexion:
                cursor = conexion.cursor()

                consulta = "SELECT idUsuarios FROM personas WHERE nombreUsuario = '{}'".format(usuario)
                cursor.execute(consulta)
                resultado = cursor.fetchone()
                numero_entero = int(resultado[0])

                consulta2 = "SELECT fk_Tipo_de_rol FROM personas_has_tipo_de_rol WHERE Personas_idUsuarios = '{}'".format(numero_entero)
                cursor.execute(consulta2)
                resultado2 = cursor.fetchone()
                
                cursor.close()
                cerrar_bd(conexion)

                return resultado2[0]

            else:
                print("No se pudo conectar a la base de datos.")
            
            cerrar_bd(conexion)
        
        except mysql.connector.Error as e:
            print("Error:", e)