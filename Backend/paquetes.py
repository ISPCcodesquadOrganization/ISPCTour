import mysql.connector
from mysql_conexion import conectar_bd, cerrar_bd
import os
import time

class Paquetes:
    def __init__(self, fechaInicio="", fechaFin="", destino="", tipoTransporte=0, cantidadViajantes=0):
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.destino = destino
        self.tipoTransporte = tipoTransporte
        self.cantidadViajantes = cantidadViajantes

    def getFechaInicio(self):
        return self.fechaInicio

    def setFechaInicio(self, fechaInicio):
        self.fechaInicio = fechaInicio

    def getFechaFin(self):
        return self.fechaFin

    def setFechaFin(self, fechaFin):
        self.fechaFin = fechaFin

    def getDestino(self):
        return self.destino

    def setDestino(self, destino):
        self.destino = destino

    def getTipoTransporte(self):
        return self.tipoTransporte

    def setTipoTransporte(self, tipoTransporte):
        self.tipoTransporte = tipoTransporte

    def getCantidadViajantes(self):
        return self.cantidadViajantes

    def setCantidadViajantes(self, cantidadViajantes):
        self.cantidadViajantes = cantidadViajantes

    def mostrarPaquetesDestino(self, idDestino):
        try:
            # Conectar a la base de datos
            conexion = conectar_bd()

            # Verificar la conexión
            if conexion:
                cursor = conexion.cursor()

                consulta = "SELECT * FROM paquetes WHERE Destino_idDestino = %s"
                cursor.execute(consulta, (idDestino,))
                resultados = cursor.fetchall()  # Obtener todos los paquetes relacionados con el destino

                cursor.close()
                cerrar_bd(conexion)

                if resultados:
                    print('_____________________________________')
                    for i, paquete in enumerate(resultados, start=1):
                        print(f"{i}. Fecha de inicio: {paquete[1]}, Fecha de fin: {paquete[2]}, Tipo de transporte: {paquete[4]}, Cantidad de viajantes: {paquete[5]}")
                    print('_____________________________________')
                    return resultados
                else:
                    print("No hay paquetes disponibles para este destino.")
            else:
                print("No se pudo conectar a la base de datos.")

        except mysql.connector.Error as e:
            print("Error:", e)

    def realizarReservaPaquete(self, codigo, usuario_id):
        try:
            # Conectar a la base de datos
            conexion = conectar_bd()

            # Verificar la conexión
            if conexion:
                cursor = conexion.cursor()

                # Comprueba que el código del paquete sea válido
                consulta_paquete = "SELECT idPaquetes FROM paquetes WHERE idPaquetes = %s"
                cursor.execute(consulta_paquete, (codigo,))
                paquete = cursor.fetchone()

                if paquete:
                    if usuario_id is not None:
                        # Insertar la reserva en la tabla de reservas
                        insertar_reserva = "INSERT INTO personas_has_paquetes (Personas_idUsuarios, Paquetes_idPaquetes) VALUES (%s, %s)"
                        cursor.execute(insertar_reserva, (usuario_id, paquete[0]))

                        # Confirmar la reserva
                        conexion.commit()
                        os.system('cls')
                        print("Reserva realizada para el paquete:", paquete[0],"!")
                        time.sleep(2)
                    else:
                        print("El usuario no existe.")
                else:
                    os.system('cls')
                    print("El código del paquete no es válido!")
                    time.sleep(1)
                    os.system('cls')

                cursor.close()
                cerrar_bd(conexion)

            else:
                print("No se pudo conectar a la base de datos.")

        except mysql.connector.Error as e:
            print("Error:", e)

