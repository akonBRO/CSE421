import socket
import global_config

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(global_config.SERVER_SOCKET_ADDR)

server.listen()
print(f"Server is listening on {global_config.SERVER_IP}:{global_config.SERVER_PORT}...")

while True:
    client_socket, client_address = server.accept() 
    
    
    message = client_socket.recv(1024).decode(global_config.EXCHANGE_FORMAT)
    
    if message:
        print(f"Client Connected: {message}")
    
    client_socket.close()