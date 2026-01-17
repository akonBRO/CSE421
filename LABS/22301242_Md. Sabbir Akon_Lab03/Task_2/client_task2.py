import socket
import global_config

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(global_config.SERVER_SOCKET_ADDR)

user_input = input("Enter a message to check vowels: ")

client.send(user_input.encode(global_config.EXCHANGE_FORMAT))
response = client.recv(1024).decode(global_config.EXCHANGE_FORMAT)
print(f"Server reply: {response}")

client.close()