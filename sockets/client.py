import socket as skt

server_host = skt.gethostbyname(skt.gethostname())
server_port = 8080

client = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
client.connect((server_host, server_port))

client.send("Message to SERVER".encode('utf-8'))