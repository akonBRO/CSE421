import socket
import global_config

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(global_config.SERVER_SOCKET_ADDR)
server.listen()
print("Vowel Counting Server Started...")

while True:
    client_socket, addr = server.accept()
    
    msg = client_socket.recv(1024).decode(global_config.EXCHANGE_FORMAT)
    
    if msg:
        num_vowels = count_vowels(msg)
        response = ""
        if num_vowels == 0:
            response = "Not enough vowels"
        elif num_vowels <= 2:
            response = "Enough vowels I guess"
        else:
            response = "Too many vowels"
            
        client_socket.send(response.encode(global_config.EXCHANGE_FORMAT))
        
    client_socket.close()