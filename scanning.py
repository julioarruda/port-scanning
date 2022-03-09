#!/usr/bin/python
import socket,sys

print ("==================Escaneamento de Portas=================")

print ("Uso: python scanning.py 192.168.68.123")

print ("IP Informado: ",sys.argv[1] )

for porta in range (1,65535):
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if meusocket.connect(sys.argv[1],porta) == 0:
        print ("Porta: ",porta, " [ABERTA]")
        meusocket.close()
