import socket
import global_config

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(global_config.SERVER_SOCKET_ADDR)

client_name = socket.gethostname()
client_ip = socket.gethostbyname(client_name)

msg_to_send = f"Device Name: {client_name}, IP: {client_ip}"

client.send(msg_to_send.encode(global_config.EXCHANGE_FORMAT))

client.close() 