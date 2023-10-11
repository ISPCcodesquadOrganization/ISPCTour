import mysql.connector
from mysql_conexion import conectar_bd, cerrar_bd


class Reserva:

   def eliminar():
     
    try:
        conexion = conectar_bd()  

        if conexion:

            cursor = conexion.cursor()
             
            eliminarReserva = input("Ingrese el numero de comprar para eliminar su reserva: ")

            sentencia = "DELETE FROM personas_has_paquetes WHERE idCompra = ('{}')".format(eliminarReserva)
            cursor.execute(sentencia)
            conexion.commit()

            cursor.close()
            cerrar_bd(conexion) 

        else:
            print("No se pudo conectar a la base de datos.")
            return []
        
    except mysql.connector.Error as e:
        print("Error:", e)
        return []

        





