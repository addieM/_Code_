__author__ = 'admirmonteiro'
from socket import _socketobject

__author__ = 'Jesus is King'

HOST, PORT = "172.30.26.220", 3723

import socket
import sys
from scipy.io.wavfile import read

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
input_data = read("Voice 005.wav")
audio = input_data[1]
print 'have connected'
try:

    # Send data
    message =  audio #'This is the message.  It will be repeated.'
    # print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)
    sock.send(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data
except:
    print('something failed sending data')
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
