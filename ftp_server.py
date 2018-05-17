#! /usr/bin/python  
# -*- coding: utf-8 -*-  
# server side  
  
import socket  
  
if __name__ == '__main__':  
    server_socket = socket.socket()  
    server_socket.bind(('0.0.0.0', 8000))  
    print ('b4 listening')  
    server_socket.listen(2)  
      
    client_socket, client_addr  = server_socket.accept()  
    print ('incoming connection')  
    if client_socket:   
        while True:  
            recv_data = client_socket.recv(20)  
            if not recv_data:  
                break;  
            if recv_data == 'g':  
                print ('sending file tmp' )
                out_file = open('tmp', 'r')  
                send_data = out_file.read()  
                client_socket.send(send_data)  
                out_file.close()  
            else:  
                print ('receiving %s' % recv_data)  
                client_socket.send(recv_data)  
    print ('end')  
    server_socket.close()  
    client_socket.close()  