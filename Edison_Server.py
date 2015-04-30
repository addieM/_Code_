__author__ = 'admirmonteiro'
__author__ = 'admirmonteiro is king for the real King'
# all of my imports
import socket
import sys
import csv
import datetime


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the port
server_address = ('', 3723)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
print>>sys.stderr, 'bind complete, no worries'

# Listen for incoming connections
sock.listen(1)
print>>sys.stderr, 'socket is now listening'

# Wait for a connection, until it is gotten
while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in bytes of 1024 bytes
        while True:
            data = connection.recv(8192) # will always return whenever it receives data
            print >>sys.stderr, 'received "%s"' % data

            if data:
              print data
                #name_File = datetime.datetime.now().time()
                # fid = open('test.csv', 'wb')
                # try:
                #     for item in data:
                #         writer = csv.writer(fid)
                #         writer.writerow(item)
                # except:
                #     print('errors happened while trying to write to the csv file')
                # connection.sendall(data)
            else:
                connection.close()
    finally:
             print >>sys.stderr, 'finished the socket'


