import socket
import threading
import global_config

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def handle_client(conn, addr):
    print(f"Connected to {addr}")
    
    connected = True
    while connected:
        try:
            msg = conn.recv(1024).decode(global_config.EXCHANGE_FORMAT)
            if not msg:
                connected = False
                break
                
            num_vowels = count_vowels(msg)
            response = ""

            if num_vowels == 0:
                response = "Not enough vowels"
            elif num_vowels <= 2:
                response = "Enough vowels I guess"
            else:
                response = "Too many vowels"
            
            conn.send(response.encode(global_config.EXCHANGE_FORMAT))
            
            connected = False 
            
        except:
            connected = False

    conn.close()
    print(f"Disconnected from {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(global_config.SERVER_SOCKET_ADDR)
server.listen()
print("Multi-threaded Vowel Server Started...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"Active connections: {threading.active_count() - 1}")