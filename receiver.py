import socket
import threading
import time


client_data = {}
def handle_client(nickname, client):
    client.send("Please Send the Filename".encode('utf-8'))
    filename = client.recv(1024).decode('utf-8')
    client.send("Please Send the File".encode('utf-8'))

    start_time = time.time()

    with open(filename, "wb") as f:
        file_data = client.recv(1048572)
        count=0
        while file_data:
            count+=1
            print(count)
            f.write(file_data)
            file_data = client.recv(1048572)

    print("File Received")    
    client_data.pop(nickname)
    end_time = time.time()

    client.send("File Received".encode('utf-8'))
    
    print(f"Time: {round(end_time - start_time,3)}")

    client.close()

def main():
    while True:
        client, client_address = server.accept()
        nickname = client.recv(1024).decode('utf-8')
        client_data[nickname] = {'client': client}
        print(f"{nickname} is waiting to send a file")
        

        thread = threading.Thread(target=handle_client, args=(nickname, client,))
        thread.start()
        

if __name__=='__main__':

    server = socket.socket()
    server.bind(('', 9920))
    server.listen(5)
    print("Receiver is Ready")

    main()
    



