import os
import time
import mysql.connector
from mysql_conexion import conectar_bd, cerrar_bd

class Destinos:
    #descrubrí que en Python no se puede sobrecargar el constructor creando uno vacio como en Java, sin embargo
    #se puede determinar valores en el único constructor posible para llamar a una funcion de la clase sin pasarle valores al constructor. 
    def __init__(self, destino="", descripcion="", precio=0, habilitado=False):
        self.destino = destino
        self.descripcion = descripcion
        self.precio = precio
        self.habilitado = habilitado
        
   
        
    def getDestinosHabilitados(self):
        try:
            # Conectar a la base de datos
            conexion = conectar_bd()  

            # Verificar la conexión
            if conexion:
                cursor = conexion.cursor()

                consulta = "SELECT * FROM destino WHERE habilitado = True"  
                cursor.execute(consulta)
                resultados = cursor.fetchall()  # Obtener todos los destinos habilitados

                cursor.close()
                cerrar_bd(conexion) 

                return resultados
            else:
                print("No se pudo conectar a la base de datos.")
                return []

        except mysql.connector.Error as e:
            print("Error:", e)
            return []




    def listarDestinosHabilitados(self):
        destinos_habilitados = self.getDestinosHabilitados()

        if not destinos_habilitados:
            print("No hay destinos habilitados disponibles.")
        else:
            print('Los destinos disponibles son los siguientes: ')
            print('_____________________________________________')
            print('')
            for i, destino in enumerate(destinos_habilitados, start=1):
                print(f"{i}. {destino[1]} - Descripción: {destino[2]} - Precio: ${destino[3]}")
            print('_____________________________________________')