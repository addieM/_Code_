__author__ = 'admirmonteiro'
__author__ = 'JESUS is Lord'
# all of my imports
import socket
import sys
import struct
import csv


# functions
def recvall(connection, count):
    buf = b''
    while count:
        newbuf = connection.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


def recv_one_message(connection):
    lengthbuf = recvall(connection, 1024)
    length, = struct.unpack('!I', lengthbuf)
    return recvall(connection, length)


def out(output):
    print >> sys.stdout, output


wavCon = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

address = ('', 3714)

print >>sys.stderr, 'Started on %s port %s' % address
wavCon.bind(address)
print>>sys.stderr, 'Bind good'

wavCon.listen(1)
print >> sys.stdout, 'Listening'

savePath = '/home/root/Coding/Python/Income_Data/waV'

while True:
    print >> sys.stdout, 'Waiting Connection'
    connection, client_Location = wavCon.accept()
    print >> sys.stdout, 'Connected to :', client_Location
    try:
        recv_one_message(connection)
    finally:
        out('connection closed')
        connection.close()



