conn = pq_connect (setdbopts ("dbname", "postgres", "host", "localhost", "port", "5432", "user", "postgres", "password", "11122000"))

angulo1 = float(input("Ingrese el primer angulo: "))
angulo2 = float(input("Ingrese el segundo angulo: "))
angulo3 = 180 - angulo1 - angulo2


N=pq_exec_params(conn,"insert into angulos values(angulo1,angulo2,angulo3,'1','2','3');")

N=pq_exec_params(conn, 'select * from angulos;')