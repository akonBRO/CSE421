import socket
import global_config

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(global_config.SERVER_SOCKET_ADDR)

hours_input = input("Enter hours worked: ")

client.send(hours_input.encode(global_config.EXCHANGE_FORMAT))

salary_msg = client.recv(1024).decode(global_config.EXCHANGE_FORMAT)
print(salary_msg)

client.close()