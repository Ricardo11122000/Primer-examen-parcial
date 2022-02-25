#CUARTO PROBLEMA 
#EXAMEN PARCIAL

import math
from random import randint
from unittest.case import doModuleCleanups
from numpy import empty
import psycopg2
import os



while True: 
    try:
        conexion = psycopg2.connect(
        host = "localhost",
        port =  "5432",
        user = "postgres", 
        password = "11122000", 
        dbname = "postgres"
    ) 
        print("Conexion exitosa")
    except psycopg2.Error as e:
        print("Conexion fallida") 


    print("menu principal: ")
    print(" ")
    print("1. Ingresar numero ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    if(opcion_escogida == "1"):

        suma = 0
        while (suma != 7 or suma!=8):
            lanzamiento1 = input("Ingrese Si o No si desea realizar el primer lanzamiento: ")
            lanzamiento2 = input("Ingrese Si o No si desea realizar el segundo lanzamiento: ")
            if(lanzamiento1 == "Si" or lanzamiento1 == "si"):
                dado1 = randint(1,6)
            else:
                break
            if(lanzamiento2 == "Si" or lanzamiento2 == "si"):
                dado2 = randint(1,6)
            else:
                break
            dado2 = randint(1,6)
            suma  = dado1 + dado2
            if(suma == 7):
                print("perdio")
                resultado = "perdio"
            if(suma == 8):
                print("gano")
                resultado = "gano"
       

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO granocho(dado1, dado2, suma, resultado) VALUES( %s,%s, %s, %s);",(dado1,dado2,suma,resultado))
        conexion.commit()
        cursor.close()
        conexion.close() 

        

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM granocho;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 