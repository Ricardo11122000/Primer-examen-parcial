#SERIE 2
#EJERCICIO 1
import math
import psycopg2


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
    print("1. Ingresar un numero ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    if(opcion_escogida == "1"):

        dia = int(input("Ingrese el dia de su nacimiento: "))
        mes = int(input("Ingrese el mes de su nacimiento: "))
        año = int(input("Ingrese el año de su nacimiento: "))



        dia_actual = 24
        mes_actual = 2
        año_actual = 2022

        if(dia > dia_actual):
            diferencia_dias = dia - dia_actual
        else:
            diferencia_dias = dia_actual - dia
        if(mes > mes_actual):
            diferencia_mes = (mes - mes_actual)*(365/12)
        else:
            diferencia_mes = (mes_actual - mes)*(365/12)
        if(año < año_actual and mes < mes_actual):
            diferencia_año = (año_actual - año)*365
        elif(año < año_actual):
            diferencia_año = (año_actual - 1 - año)*365
        else:
            diferencia_año = (año - año_actual)*365
        if(dia > dia_actual and mes > mes_actual):
            print("Su cumpleaños ya ha sido")
        if(mes < mes_actual):
            print("Su cumpleaños aun no ha sido")

        print(diferencia_dias)
        print(diferencia_mes)
        print(diferencia_año)

        diferencia_total = diferencia_dias + diferencia_mes + diferencia_año

        diferencia_total = diferencia_total/365
        diferencia_total = math.floor(diferencia_total)

        print("Su edad es: ", diferencia_total)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO edad(año, mes,dia,edad) VALUES( %s,%s,%s,%s);",(año,mes,dia,diferencia_total))
        conexion.commit()
        cursor.close()
        conexion.close() 

    elif(opcion_escogida == "2"):

        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM edad;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    elif(opcion_escogida == "3"):
        exit()



