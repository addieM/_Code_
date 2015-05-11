__author__ = 'admirmonteiro'
from socket import _socketobject

__author__ = 'Jesus is King'

HOST, PORT = "192.168.0.105", 3714

import socket
import sys
from scipy.io.wavfile import read

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
input_data = open('data.txt', 'r')
print 'have connected'
print 'sending...'
message =  input_data.read(1024) #'This is the message.  It will be repeated.'
try:
    # Send data
    # message =  input_data.read(1024) #'This is the message.  It will be repeated.'
    # print >>sys.stderr, 'sending "%s"' % message
    # sock.sendall(message)
    print message
    while message:
        sock.send(message)
        # print message
        message = input_data.read(1024)
except:
    print('something failed sending data')
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()



# while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)
    #     print >>sys.stderr, 'received "%s"' % data