__author__ = 'admirmonteiro'
__author__ = 'admirmonteiro is king for the real King'
# all of my imports
import socket
import sys
import csv
import os
# import datetime
# import _struct
# import time


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the port
server_address = ('', 3714)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
print>>sys.stderr, 'bind complete, no worries'

# Listen for incoming connections : but one can be connect
sock.listen(1)
print>>sys.stderr, 'socket is now listening'
savePath = '/home/root/Coding/Python/Income_Data'
# Wait for a connection, until it is gotten
while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    print >>sys.stderr, 'connection from', client_address
    try:
        f = open('file.txt', 'wb')
        while True:
        # Receive the data in bytes of 1024 bytes
            data = connection.recv(1024) # will always return whenever it receives data\
            # print 'printed before write: '+ data
            if not data:
                print'no more data'
                break
                print 'stuck'
                f.close()
                print('2')
            else:
                f.write(data)
                data = connection.recv(1024)

    finally:
        connection.close()
        print >>sys.stderr, 'Socket Closed: Will seek new Connection'

