import socket as skt

host = skt.gethostbyname(skt.gethostname())
port = 8080

server_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

comm_socket, address = server_socket.accept()

message = comm_socket.recv(1024)
print(message)
message = message.decode('utf-8')
print(message)
