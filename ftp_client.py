#! /usr/bin/python  
# -*- coding: utf-8 -*-  
# client side  
  
import socket  
  
if __name__ == '__main__':  
    client_socket = socket.socket()  
    client_socket.connect(('127.0.0.1', 8000)) #根据需要更改地址  
    print ('connected')  
    while True:  
        print ('sending data')  
        in_data = raw_input('>>')  
        if in_data == 'q':  
            break;  
        client_socket.send(in_data)  
        recv_data = client_socket.recv(1024)  
        if in_data == 'g': #获取tmp文件内容的前1024字节写入本地文件  
            f = open('tmp', 'w')  
            f.write(recv_data)  
            f.close()  
        if recv_data:  
            print ('from server %s' % recv_data)  
        else:  
            break  
    print 'end'  
    client_socket.close()  