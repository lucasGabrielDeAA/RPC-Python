#coding: utf-8

##Servidor para realizar a chamada dos métodos da classe Opereções
import socket

PORTA = 6666

IP = '10.3.5.20'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORTA))

s.listen(1)

def fatorial(numero):
    if numero == 1:
        return numero
    elif numero < 0:
        return 0
    else:
        return numero * fatorial(numero-1)

while True:
    print '\nAguardando Conexão...\n\n'

    con, info_cli = s.accept()

    print 'Conexão estabelecida pelo Host ',info_cli, '\n\n'

    dados_recebidos = con.recv(1024)

    argumentos = dados_recebidos.split()

    if argumentos[0] == 'soma':
        dados = int(argumentos[1]) + int(argumentos[2])
        con.send(str(dados))

    elif argumentos[0] == 'produto':
        dados = int(argumentos[1]) * int(argumentos[2])
        con.send(str(dados))

    elif argumentos[0] == 'fatorial':
        fat = fatorial(int(argumentos[1]))
        con.send(str(fat))

con.close()
