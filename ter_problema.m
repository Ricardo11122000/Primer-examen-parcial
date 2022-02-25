conn = pq_connect (setdbopts ("dbname", "postgres", "host", "localhost", "port", "5432", "user", "postgres", "password", "11122000"))

numero = float(input("Ingrese un numero: "))
centenas=(numero%1000-numero%100)
decenas=(numero%100-numero%10)
unidades=numero%10 




N=pq_exec_params(conn,"insert into cifras values(numero,unidades,decenas,centenas,'1','2','3','4');")

N=pq_exec_params(conn, 'select * from cifras;')