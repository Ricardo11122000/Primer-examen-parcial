#SEGUNDO PROBLEMA
# EXAMEN PARCIAL

import math
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
    print("1. Ingresar ANGULOS ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    if(opcion_escogida == "1"):

        angulo1 = float(input("Ingrese el primer angulo: "))
        angulo2 = float(input("Ingrese el segundo angulo: "))
        angulo3 = 180 - angulo1 - angulo2

       

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO angulos(angulo1, angulo2, angulo3) VALUES( %s,%s, %s);",(angulo1,angulo2,angulo3))
        conexion.commit()
        cursor.close()
        conexion.close() 

        

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM angulos;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 