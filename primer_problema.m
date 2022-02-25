conn = pq_connect (setdbopts ("dbname", "postgres", "host", "localhost", "port", "5432", "user", "postgres", "password", "11122000"))

dia_actual = 24
mes_actual = 2
ano_actual = 2022

dia = input("Ingrese el dia de su nacimiento: ")
mes = input("Ingrese el mes de su nacimiento: ")
ano = input("Ingrese el año de su nacimiento: ")

if(dia > dia_actual):
 diferencia_dias = dia - dia_actual
else:
 diferencia_dias = dia_actual - dia
if(mes > mes_actual):
 diferencia_mes = (mes - mes_actual)*(365/12)
else:
 diferencia_mes = (mes_actual - mes)*(365/12)
if(ano < ano_actual and mes < mes_actual):
 diferencia_ano = (ano_actual - ano)*365
elif(ano < ano_actual):
 diferencia_ano = (ano_actual - 1 - ano)*365
else:
 diferencia_ano = (ano - ano_actual)*365
if(dia > dia_actual and mes > mes_actual):
 print("Su cumpleaños ya ha sido")
if(mes < mes_actual):
 print("Su cumpleaños aun no ha sido")

diferencia_total = diferencia_dias + diferencia_mes + diferencia_ano

diferencia_total = diferencia_total/365
diferencia_total = math.floor(diferencia_total)

N=pq_exec_params(conn,"insert into edad values(año, mes,dia,diferencia_total,'1','2','3','4');")

N=pq_exec_params(conn, 'select * from edad;')