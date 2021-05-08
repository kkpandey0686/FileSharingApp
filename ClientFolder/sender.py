import socket
import os

def main():
    client.send(f"{nickname}".encode('utf-8'))
    print(client.recv(1024).decode('utf-8')) 

    while True:
        filename = input("Enter the Filename: ")
        if os.path.isfile(filename):
            client.send(f"{filename}".encode('utf-8'))
            print(client.recv(1024).decode('utf-8'))
            
            with open(filename, "rb") as f:
                data = f.read()
                client.sendall(data)
            break

        else :
            print(f"File with name {filename} doesn't exist")
            
    print("File Sent")
    

if __name__ == '__main__':
    
    nickname = input("Enter your nickname: ")
    client = socket.socket()
    client.connect(('127.0.0.1',9920))

    main()
    client.close()