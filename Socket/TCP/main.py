import socket

resp = "S"

while(resp == "S"):
    url = input("Url:")
    ip = socket.gethostbyname(url)
    print("Number of ip is: ", ip)
    resp = input("Deseja continuar: [s/n] ").upper
    