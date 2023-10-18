import mysql.connector
from mysql_conexion import conectar_bd, cerrar_bd
from persona import Persona


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

                consulta2 = "SELECT fk_Tipo_de_rol FROM `personas_has_tipo de rol` WHERE Personas_idUsuarios = '{}'".format(numero_entero)
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

    def modificar_rol():
        while True:
            eleccion = input('Conoce el nombre de usuario que sea modificar? SI/NO: ')

            if eleccion.lower() == 'si':
                print('Escriba el nombre del usuario')
                Administrador.cambio_rol()
                
            elif eleccion.lower() == 'no':
                print('Lista con todos los nombres de usuario')
                print('*********')

                try:
            # Conectar a la base de datos
                    conexion = conectar_bd()

                    # Verificar la conexión
                    if conexion:
                        cursor = conexion.cursor()

                        mostrar = "select nombreUsuario from personas;"
                        cursor.execute(mostrar)
                        lista_usuarios = cursor.fetchall()

                        for i in lista_usuarios:
                            print(i[0])

                        cursor.close()
                        cerrar_bd(conexion)
                        Administrador.cambio_rol()

                    else:
                        print("No se pudo conectar a la base de datos.")
                    
                    cerrar_bd(conexion)
        
                except mysql.connector.Error as e:
                    print("Error:", e)
                break
            else:
                print('Seleccione una opcion valida')
            
            

    def cambio_rol():

        while True:
            try:

                nombreUsuario = input("Ingrese un nombre de usuario: ")
                try:
                    conexion = conectar_bd()

                    # Verificar la conexión
                    if conexion:
                        cursor = conexion.cursor()

                        # Consulta SQL para verificar si el usuario existe en la tabla Personas
                        consulta = "SELECT idUsuarios FROM personas WHERE nombreUsuario = '{}'".format(nombreUsuario)
                        cursor.execute(consulta)
                        resultado = cursor.fetchone()

                        
                        resultado = resultado[0]
                        print(resultado)
                                    
                        while True:
                            print('Roles: ')
                            print('1 - Administrador')
                            print('2 - Coordinador')
                            print('3 - Usuario')
                            nuevo_rol = input('Indique el numero del nuevo rol que sea para el usuario: ')
                            nuevo_rol = int(nuevo_rol)
                            if nuevo_rol == 1 or nuevo_rol == 2 or nuevo_rol == 3:
                                print('Se modifica rol')
                                sentencia = "UPDATE `personas_has_tipo de rol` SET fk_Tipo_de_rol = '{}' WHERE Personas_idUsuarios = '{}'".format(nuevo_rol, resultado)
                                cursor.execute(sentencia)
                                conexion.commit()
                                break
                            else:
                                print('Ingrese un valor valido.')

                        

                    else:
                        print("No se pudo conectar a la base de datos.")

                    cerrar_bd(conexion)
                    print('El rol del usuario se ha modificado con exito')
                    
                
                    
                        
                except mysql.connector.Error as e:
                    print("Error:", e)
                
                
            
            except TypeError:
                print('Ingrese un nombre de usuario valido')
            print('*********')

            break

