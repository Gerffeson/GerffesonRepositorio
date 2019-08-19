import mysql.connector

connection = mysql.connector.connect(
    host='localhost', user='root', password='', database='projetovectra', charset='utf8')
cursor = connection.cursor(dictionary=True)

Name = input('Digite o nome da avenida:')
print()
Extensaoo = float(input('Digite sua extensão:'))
print()
Possui = bool(input('A avenida possui ciclo faixa?'))
print()
Ciclofaixa = float(input('Digite a extensão da ciclo faixa'))
print()

if (Possui == 'Sim'):
    cursor.execute("INSERT INTO projeto_web(Nome, Extensão, Extensão_da_ciclofaixa) VALUES('{}', {}, {})".format(
        Name, Extensaoo, Ciclofaixa))
    connection.commit()


else:
    cursor.execute(
        "INSERT INTO projeto_web(Nome, Extensão) VALUES('{}, {})".format(Name, Extensaoo))
    connection.commit()
