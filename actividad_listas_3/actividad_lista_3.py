import os 
import time

os.system('cls')

nombres = []

opc = ""


print("Bienvenido")
while True:
    print("¿Desea Ingresar un nombre?")
    opc= input("Ingrese su respuesta: ")
    

    if opc.lower()== 'si':
        os.system('cls')
        nombre = input("Ingrese Un Nombre: ")
        nombres.append(nombre)
        print(f"NOMBRE {nombre} AGREGADO!")
        time.sleep(2)
       


    elif opc.lower()== "no":
        nombre_corto = min(nombres,key = len)
        nombres.remove(nombre_corto)
        print(f"Los nombres son: {nombres}")
        print(f"Nombre eliminado: {nombre_corto}")
        break

    else:
        os.system('cls')
        print("ERROR! RESPUESTA INVÁLIDA")
        print("RESPUESTA DEBE SER SI O NO")
        time.sleep(1)