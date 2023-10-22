import mysql.connector
from mysql_conexion import conectar_bd, cerrar_bd


def comprobarId(numero):
   
    try:
      
      conexion = conectar_bd()

      if conexion:

        id_compra = numero

        cursor = conexion.cursor()

        cliente = input("Ingrese su nombre de usuario")
        consulta = "SELECT idUsuarios FROM personas WHERE nombre = '{}'".format(cliente)
        cursor.execute(consulta)
        resultado = cursor.fetchone()
        print(resultado)

        
        id_usuario = resultado[0]

        consulta2 = "SELECT Personas_idUsuarios FROM personas_has_paquetes WHERE idCompra = '{}'".format(id_compra)
        cursor.execute(consulta2)
        resultado2 = cursor.fetchone()

        cursor.close()
        cerrar_bd(conexion) 

        if id_usuario == resultado2[0]:
           return True
        else:
          print("Usted no tiene permiso para eliminar esa reserva: ")
          return False

       

      else:
        print("No se pudo conectar a la base de datos.")
        return []
      
       


    except mysql.connector.Error as e:
        print("Error:", e)
        return []

        
    
 

class EliminarReserva:

   def eliminar():
     
    try:
        conexion = conectar_bd()  

        if conexion:

            try:
                cursor = conexion.cursor()

                eliminarReserva = input("Ingrese el número de compra para eliminar su reserva: ")

                comprobar = comprobarId(eliminarReserva)

                if comprobar == True:
                    sentencia = "DELETE FROM personas_has_paquetes WHERE idCompra = ('{}')".format(eliminarReserva)
                    cursor.execute(sentencia)
                    conexion.commit()

                cursor.close()
                cerrar_bd(conexion)

            except Exception as e:
                print("El numero de compra ingresado no corresponde a un numero valido para el usuario")
           
        else:
            print("No se pudo conectar a la base de datos.")
            return []
        
    except mysql.connector.Error as e:
        print("Error:", e)
        return []