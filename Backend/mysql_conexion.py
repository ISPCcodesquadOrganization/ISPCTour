import mysql.connector


def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="ispc_tour"
        )
        if conexion.is_connected():
            return conexion
    except mysql.connector.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

def cerrar_bd(conexion):
    if conexion is not None:
        conexion.close()

