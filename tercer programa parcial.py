#TERCER PROBLEMA
#EXAMEN PARCIAL

import math
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

        numero = float(input("Ingrese un numero: "))
        centenas=(numero%1000-numero%100)
        decenas=(numero%100-numero%10)
        unidades=numero%10 

       

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO cifras(numero, unidades, decenas, centenas) VALUES( %s,%s, %s, %s);",(numero,unidades,decenas,centenas))
        conexion.commit()
        cursor.close()
        conexion.close() 

        

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM cifras;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 