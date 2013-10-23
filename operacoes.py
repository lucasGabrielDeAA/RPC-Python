#coding: utf-8

##Criação da classe que define os métodos para a realização das operações

import socket

PORTA = 6666

IP = '10.3.5.20'

class Operacoes:

	def __init__(self, ip):
		self.ip = ip
	
	def soma(self, numero1, numero2):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		s.connect((IP, PORTA))

		s.send('soma ' + str(numero1) + ' ' + str(numero2))

		dados_recebidos = s.recv(1024)

		s.close()

		return int(dados_recebidos)

	def produto(self, numero1, numero2):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		s.connect((IP, PORTA))

		s.send('produto ' + str(numero1) + ' ' + str(numero2))

		dados_recebidos = s.recv(1024)

		s.close()

		return int(dados_recebidos)

	def fatorial(self, numero):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		s.connect((IP, PORTA))

		s.send('fatorial ' + str(numero))

		dados_recebidos = s.recv(1024)

		s.close()

		return int(dados_recebidos)






##Método main
if __name__ == "__main__":

	op = Operacoes(IP)

	entrada1 = raw_input("Primeiro Número:")

	numero1 = int(entrada1)

	entrada2 = raw_input("Primeiro Número:")

	numero2 = int(entrada2)

	print "Valor Da Soma", op.soma(numero1, numero2), '\n'

	print "Valor Do Produto", op.produto(numero1, numero2), '\n'

	entrada3 = raw_input("Número Para o Fatorial:")

	numero3 = int(entrada3)

	print "Valor Do Fatorial:", op.fatorial(numero3), '\n'


