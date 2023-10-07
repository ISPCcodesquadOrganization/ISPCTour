import os
import time
from persona import Persona

os.system('cls')

def verificar_Si_No(respuesta):
    if respuesta.lower() == 'si':
        return respuesta.lower()
    elif respuesta.lower() == 'no':
        return respuesta.lower()
    else:
        os.system('cls')
        print('Seleccione una respuesta valida.')
        return verificar_Si_No(input('Por favor seleccione entre SI o NO: '))

def validar_numero():
    while True:
        numero = input("Por favor, ingresa su eleccion: ")
        if numero == '1' or numero == '2' or numero == '3' or numero == '4':
            return numero
        else:
            print("Por favor, selecciona un número válido.")



def iniciarPrograma():
    
    while True:
        
        print('***************************************************')
        print('****Bienvenido al sistema de ventas de ISPC TOUR***')
        print('***************************************************')
        print(' ')

        while True:
            respuestaUsuario = verificar_Si_No(input('Posee un usuario registrado? SI/NO: '))
            if respuestaUsuario == 'si':
                for intento in range(3):
                    validar_usuario = Persona.verificar_usuario(respuestaUsuario)
                    if validar_usuario != False:
                        os.system('cls')
                        print('Bienvenido ', validar_usuario, '!')
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

        while respuestaUsuario != False:
            print('Por favor seleccione el numero de la opción que desee realizar.')
            print('1 - Ver paquetes de viajes disponibles.')
            print('2 - Ver mis reservas.')
            print('3 - Eliminar alguna reserva')
            print('4 - Terminar sesión')

            seleccion_menu = validar_numero()

            if seleccion_menu == '1':
                print('Muestra destinos turísticos disponibles')
                print('********')
    
            elif seleccion_menu == '2':
                print('En caso de tener reservas muestra las mismas y si no muestra "No tiene reservas"')
                print('********')
    
            elif seleccion_menu == '3':
                print('Muestra las reservas y da la opción de eliminarlas')
                print('********')
    
            else:
                print('Sesión cerrada')
                print('********')
                break
        os.system('cls')
        iniciarPrograma()

   
iniciarPrograma()