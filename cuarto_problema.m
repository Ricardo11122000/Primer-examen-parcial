conn = pq_connect (setdbopts ("dbname", "postgres", "host", "localhost", "port", "5432", "user", "postgres", "password", "11122000"))

suma = 0
        while (suma != 7 | suma!=8):
            lanzamiento1 = input("Ingrese Si o No si desea realizar el primer lanzamiento: ")
            lanzamiento2 = input("Ingrese Si o No si desea realizar el segundo lanzamiento: ")
            if(lanzamiento1 == "Si" or lanzamiento1 == "si"):
                dado1 = randint(1,6)
            else:
                break
            if(lanzamiento2 == "Si" | lanzamiento2 == "si"):
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


N=pq_exec_params(conn,"insert into granocho values(dado1,dado2,suma,resultado,'1','2','3'3,'4');")

N=pq_exec_params(conn, 'select * from granocho;')