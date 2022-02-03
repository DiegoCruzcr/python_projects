from socket import *

servidor = '127.0.0.1' #localhost
porta = 43210
obj_socket = socket(AF_INET,  SOCK_STREAM) #type connection ip, tcp
obj_socket.bind((servidor, porta))
obj_socket.listen(2) #limitclients

print("Aguardando cliente...")

while True:
    con, client = obj_socket.accept()
    print("Conectado com: ", client)
    while True:
        msg_recv = str(con.recv(1024))
        print("Msg recebida: ", msg_recv)
        msg_send = b'Hello client'
        con.send(msg_send)
        break
    con.close()