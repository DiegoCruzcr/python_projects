from socket import *

server = '127.0.0.1' #localhost
port = 43210 #port to conexion

msg = bytes(input("Digite algo: "), 'utf-8') #codifing to utf-8 and transforming in bytes
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((server, port))
obj_socket.send(msg)
response = obj_socket.recv(1024)
print(f"Recebemos:{response}")
obj_socket.close()