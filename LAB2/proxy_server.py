#!/usr/bin/env python3
import socket
import os

#define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    # create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(3)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            pid = os.fork()
            if pid == 0:
                #connect to google.com
                client_socket.connect((socket.gethostbyname("www.google.com"), 80))
                
                #recieve data from client
                full_data = conn.recv(BUFFER_SIZE)
                print("Data from client: ", full_data.decode())

                #send to google
                client_socket.sendall(full_data)

                #get response from google
                client_data = b""
                while True:
                    data = client_socket.recv(BUFFER_SIZE)
                    if not data:
                        break
                    client_data += data
                
                print("Response from google: ", client_data.decode())
                #send it back to the client
                conn.sendall(client_data)

                client_socket.close()
                conn.close()
                os._exit(0)
            else:
                conn.close()
            

if __name__ == "__main__":
    main()
