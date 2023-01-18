#!/usr/bin/env python3
import socket
import time
import sys

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
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)

            #connect to google.com
            client_socket.connect((socket.gethostbyname("www.google.com"), 80))
            
            #recieve data from client
            full_data = conn.recv(BUFFER_SIZE)

            #send to google
            client_socket.sendall(full_data)

            #get response from google
            client_data = b""
            while True:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                client_data += data
            
            #send it back to the client
            conn.sendall(client_data)
            conn.close()

if __name__ == "__main__":
    main()
