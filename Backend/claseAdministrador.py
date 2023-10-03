import mysql.connector
from persona import Persona  

class Administrador(Persona):
    def __init__(self, id_empleado):
        super().__init__()  
        self.id_empleado = id_empleado
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ispctour"
        )

    def agregar_destino(self, nombre_destino):
        try:
            cursor = self.conexion.cursor()

           
            cursor.execute("INSERT INTO Destino (nombreDestino) VALUES (%s)", (nombre_destino,))
            self.conexion.commit()
            print(f"Destino '{nombre_destino}' agregado correctamente.")

        except mysql.connector.Error as e:
            print("Error al agregar el destino:", e)

    

        finally:
            cursor.close()
    
    def eliminar_destino(self):
        try:
            cursor = self.conexion.cursor()

            
            cursor.execute("SELECT idDestino, nombreDestino FROM Destino")
            destinos = cursor.fetchall()

            if not destinos:
                print("No hay destinos para eliminar.")
                return

            print("Destinos disponibles:")
            for id_destino, nombre_destino in destinos:
                print(f"{id_destino}: {nombre_destino}")

            id_a_eliminar = input("Ingrese el ID del destino que desea eliminar: ")

            if not id_a_eliminar.isdigit():
                print("ID no válido.")
                return

            id_a_eliminar = int(id_a_eliminar)

            cursor.execute("DELETE FROM Destino WHERE idDestino = %s", (id_a_eliminar,))
            self.conexion.commit()
            print(f"Destino con ID {id_a_eliminar} eliminado correctamente.")

        except mysql.connector.Error as e:
            print("Error al eliminar el destino:", e)

        finally:
            cursor.close()
    
    def modificar_tipo_rol(self):
        try:
            cursor = self.conexion.cursor()

            cursor.execute("SELECT p.idUsuario, p.nombre, p.apellido, r.idTipoDeRol, r.Rol FROM Personas p JOIN TipoDeRol r ON p.idTipoDeRol = r.idTipoDeRol")
            usuarios = cursor.fetchall()

            if not usuarios:
                print("No hay usuarios para modificar.")
                return

            print("Usuarios disponibles:")
            for id_usuario, nombre, apellido, id_tipo_rol, rol in usuarios:
                print(f"{id_usuario}: {nombre} {apellido}, Rol: {rol} (ID Tipo de Rol: {id_tipo_rol})")

            id_a_modificar = input("Ingrese el ID del usuario que desea modificar: ")

            if not id_a_modificar.isdigit():
                print("ID no válido.")
                return

            id_a_modificar = int(id_a_modificar)

            cursor.execute("SELECT idTipoDeRol, Rol FROM TipoDeRol")
            tipos_rol = cursor.fetchall()

            if not tipos_rol:
                print("No hay tipos de rol disponibles.")
                return

            print("Tipos de Rol disponibles:")
            for id_tipo_rol, rol in tipos_rol:
                print(f"{id_tipo_rol}: {rol}")

            nuevo_id_tipo_rol = input("Ingrese el nuevo ID Tipo de Rol: ")

            if not nuevo_id_tipo_rol.isdigit():
                print("Nuevo ID Tipo de Rol no válido.")
                return

            nuevo_id_tipo_rol = int(nuevo_id_tipo_rol)

            cursor.execute("UPDATE Personas SET idTipoDeRol = %s WHERE idUsuario = %s", (nuevo_id_tipo_rol, id_a_modificar))
            self.conexion.commit()
            print(f"ID Tipo de Rol del usuario con ID {id_a_modificar} modificado correctamente a {nuevo_id_tipo_rol}.")

        except mysql.connector.Error as e:
            print("Error al modificar el tipo de rol:", e)

        finally:
            cursor.close()