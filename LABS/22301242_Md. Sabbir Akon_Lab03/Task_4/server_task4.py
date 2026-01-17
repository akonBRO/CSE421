import socket
import global_config

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(global_config.SERVER_SOCKET_ADDR)
server.listen()
print("Salary Calculation Server Started...")

while True:
    client_socket, addr = server.accept()
    
    hours_str = client_socket.recv(1024).decode(global_config.EXCHANGE_FORMAT)
    
    if hours_str:
        try:
            hours = float(hours_str)
            salary = 0.0

            if hours <= 40:
                salary = hours * 200
            else:
                extra_hours = hours - 40
                salary = 8000 + (extra_hours * 300)
            
            response = f"Salary: Tk {salary}"
            client_socket.send(response.encode(global_config.EXCHANGE_FORMAT))
            
        except ValueError:
            client_socket.send("Invalid input".encode(global_config.EXCHANGE_FORMAT))
            
    client_socket.close()