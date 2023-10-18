import os
import time
from destinos import Destinos
from persona import Persona
from paquetes import Paquetes
from administrador import Administrador
from mysql_conexion import conectar_bd, cerrar_bd  # Importar la función conectar_bd
from destinos_Administrar import Administrar_destinos
os.system('cls')


def verificar_Si_No(respuesta):
    if respuesta.lower() == 'si':
        return respuesta.lower()
    elif respuesta.lower() == 'no':
        return respuesta.lower()
    else:
        os.system('cls')
        print('Seleccione una respuesta válida.')
        return verificar_Si_No(input('Por favor seleccione entre SI o NO: '))

def validar_numero():
    while True:
        numero = input("Por favor, ingrese su elección: ")
        if numero in ['1', '2', '3', '4','5']:
            return numero
        else:
            print("Por favor, seleccione un número válido.")

def iniciarPrograma():
    while True:
        print('***************************************************')
        print('****Bienvenido al sistema de ventas de ISPC TOUR***')
        print('***************************************************')
        print(' ')
        
        while True:
            
            respuestaUsuario = verificar_Si_No(input('¿Posee un usuario registrado? SI/NO: '))
            if respuestaUsuario == 'si':
                for intento in range(3):
                    validar_usuario = Persona.verificar_usuario(respuestaUsuario)
                    if validar_usuario != False:
                        os.system('cls')
                        print('Bienvenido', validar_usuario, '!')
                        break
                    else:
                        os.system('cls')
                        print('Contraseña incorrecta. Te quedan', 2 - intento, 'intentos.')

                    if intento == 2:
                        os.system('cls')
                        print("Múltiples intentos fallidos, no aceptamos robots!")
                        respuestaUsuario = False
                        time.sleep(2)
                        break

                break

            else:
                os.system('cls')
                print('Menu registro')
                nuevoUsuario = Persona()
                print('El sistema va a reiniciar, seleccione la opción SI al inicio del programa.')
                print('Y a continuación ingrese su usuario registrado')
                print('*********')
                time.sleep(3)
                os.system('cls')

        if Administrador.verificarAdministrador(validar_usuario) == 1:

            while True:
                print('******************************')
                print('Bienvenido al menu de administrador')
                print('******************************')
                print('1 - Cambiar rol de usuario')
                print('2 - Agregar destino')
                print('3 - Editar destino')
                print('4 - Salir de menu de administrador y pasar al menu normal')

                seleccion_administrador = input('Ingrese la opcion seleccionada: ')

                if seleccion_administrador == '1':
                    print('Permite seleccionar usuarios para editar')
                    Administrador.modificar_rol()
                    print('********')
            
                elif seleccion_administrador == '2':
                    print('Opciones para agregar destinos')
                    nuevo_destino = Administrar_destinos()
                    
                    print('********')
            
                elif seleccion_administrador == '3':
                    print('Muestra destinos y permite seleccionar uno para editar')
                    Administrar_destinos.editarDestino()
                    
                    print('********')
            
                elif seleccion_administrador == '4':
                    print('Usted ha salido de menu administrador')
                    print('********')
                    break

                else:
                    print('La opcion seleccionada no es valida')
                    print('********')

        while respuestaUsuario != False:
            print('Por favor seleccione el número de la opción que desee realizar.')
            print('***************************************************************')
            print('')
            print('1 - Ver destinos disponibles.')
            print('2 - Realizar reserva.')
            print('3 - Ver mis reservas.')
            print('4 - Eliminar alguna reserva')
            print('5 - Terminar sesión')

            seleccion_menu = validar_numero()

            if seleccion_menu == '1':
                os.system('cls')
                destinos = Destinos()
                destinos.listarDestinosHabilitados()
                time.sleep(1)

                respuestaUsuario = verificar_Si_No(input('¿Desea ver paquetes de un destino? SI/NO: '))
                if respuestaUsuario == 'si':
                    os.system('cls')
                    destino = destinos.seleccionarDestino()

                    if destino:
                        print(f"Los paquetes disponibles para {destino[1]} son:")
                        paquetes = Paquetes()
                        resultados_paquetes = paquetes.mostrarPaquetesDestino(destino[0])

                        if resultados_paquetes:
                            while True:
                                try:
                                    opcion_paquete = int(input("Seleccione el paquete que desearía reservar o está interesado (ingrese el número): "))
                                    if 1 <= opcion_paquete <= len(resultados_paquetes):
                                        paquete_elegido = resultados_paquetes[opcion_paquete - 1]
                                        os.system('cls')
                                        print("El paquete elegido es","CODIGO: ", paquete_elegido[0],". Tome nota del mismo para la reserva")
                                        print('')
                                        
                                        break
                                    else:
                                        print("Opción no válida. Por favor, seleccione un número válido.")
                                except ValueError:
                                    print("Por favor, ingrese un número válido.")
                        else:
                            print("No hay paquetes disponibles para este destino.")
                    else:
                        time.sleep(1)
                        os.system('cls')

                else:
                    print('NO HAY PROBLEMA')
                    time.sleep(1)
                    os.system('cls')

            
            elif seleccion_menu == '2':
                print('Hacer una reserva')
                print('*****************')
                print('')
                print('Usted está por realizar una reserva.')
                print('Ingrese el CÓDIGO del paquete a reservar: ')
                
                codigo = input()
                
                                         
                paquetes = Paquetes()
                usuario = validar_usuario
                paquetes.realizarReservaPaquete(codigo, usuario)
                               
            
            elif seleccion_menu == '3':
                verMisReservas()

            elif seleccion_menu == '4':
                print('Muestra las reservas y da la opción de eliminarlas')
                print('********')

            else:
                os.system('cls')
                cerrar_bd
                print('Sesión cerrada, gracias por usar nuestro sistema.')
                print('********')
                time.sleep(2)
                
                break
        os.system('cls')
        iniciarPrograma()

iniciarPrograma()
