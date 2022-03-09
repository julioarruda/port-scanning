#!/usr/bin/python
import socket,sys

print ("==================Escaneamento de Portas=================")

print ("Uso: python scanning.py 192.168.68.123 123")

print ("IP Informado: ",sys.argv[1] )

IP=sys.argv[1]
PORT=int(sys.argv[2])

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if (meusocket.connect_ex((IP,PORT)) == 0):
    banner = meusocket.recv(1024)
    print ("Porta: ",PORT, " [ABERTA] - Banner: ", banner)        
    meusocket.close()
