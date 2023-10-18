import mysql.connector
from mysql_conexion import conectar_bd, cerrar_bd


class Administrar_destinos:
    def __init__(self):
        self.destino = input('Nombre del nuevo destino: ')
        self.descripcion = input('Descripcion: ')
        self.precio = input('Ingrese el precio del destino: ')
        self.habilitado = input('Ingrese "1" si desea que el paquete este habilitado, de lo contrario coloque "0": ')
        
        try:
            # Conectar a la base de datos
            conexion = conectar_bd()

            # Verificar la conexión
            if conexion:
                cursor = conexion.cursor()

                sentencia = "INSERT INTO destino (nombreDestino, descripcion, precio, habilitado) VALUES ('{}', '{}', '{}', '{}')".format(self.destino,self.descripcion,self.precio, self.habilitado)
                cursor.execute(sentencia)
                conexion.commit()

                

                cursor.close()
                cerrar_bd(conexion)

            else:
                print("No se pudo conectar a la base de datos.")
            
            cerrar_bd(conexion)
        
        except mysql.connector.Error as e:
            print("Error:", e)

    def mostrarDestinosAdministrador():
        try:
            # Conectar a la base de datos
            conexion = conectar_bd()  

            # Verificar la conexión
            if conexion:
                cursor = conexion.cursor()

                consulta = "SELECT * FROM destino"  
                cursor.execute(consulta)
                resultados = cursor.fetchall()  # Obtener todos los destinos habilitados
                #print(resultados)

                for i in resultados:
                    print('ID destino: ', i[0])
                    print('Nombre destino: ', i[1])
                    print('Descripcion: ', i[2])
                    print('Precio: ', i[3])
                    print('Estado(1- habilitado, 0 - deshabilitado): ', i[4])
                    print('_____________________________________________')

                cursor.close()
                cerrar_bd(conexion) 

                #return resultados
            else:
                print("No se pudo conectar a la base de datos.")
                return []

        except mysql.connector.Error as e:
            print("Error:", e)
            return []
        

    def editarDestino():
        print('Acontinuacion se mostraran todos los destinos existentes')
        print('Por favor seleccione el ID del que desea editar')
        Administrar_destinos.mostrarDestinosAdministrador()
        while True:
            try:
                
                destino_editar = int(input('Ingrese el ID de destino a editar: '))
                conexion = conectar_bd()

                if conexion:
                    cursor = conexion.cursor()
                    consulta = "SELECT COUNT(*) FROM destino WHERE idDestino = '{}'".format(destino_editar)
                    cursor.execute(consulta)
                    resultado = cursor.fetchone()

                    if resultado[0] > 0:
                        try:
                            nuevo_nombre = input('Ingrese el nuevo nombre del destino: ')
                            nueva_descripcion = input('Ingrese la nueva descripcion: ')
                            nuevo_precio = int(input('Ingrese el nuevo valor del destino: '))
                            nuevo_estado = int(input('Ingrese "1" si quiere que el destino se encuentre disponible o "0" en caso contrario: '))

                            
                            sentencia = "UPDATE destino SET nombreDestino = '{}', descripcion = '{}', precio = {}, habilitado = {} WHERE idDestino = '{}'".format(nuevo_nombre, nueva_descripcion, nuevo_precio, nuevo_estado, destino_editar)
                            cursor.execute(sentencia)
                            conexion.commit()
                            print('Destino editado exitosamente')
                            print('_____________________________________________')
                            break
                        except ValueError:
                            print('Ingrese numeros validos para precio y estado')
                        break


                cerrar_bd(conexion)
            except ValueError:
                print('Ingrese un número válido para el ID de destino.')
                print('_____________________________________________')