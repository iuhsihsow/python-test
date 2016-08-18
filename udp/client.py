import socket
port = 8081
host = "localhost"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "Hello word!"
s.sendto(data.encode("utf-8"), (host, port))