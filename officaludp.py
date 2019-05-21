import socket
import signal
import sys
 
def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sock.close()
    sys.exit(0)
 
signal.signal(signal.SIGINT, signal_handler)
 
ECHO_PORT = 7
 
print 'Server Running at ', socket.gethostbyname(socket.gethostname()) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', ECHO_PORT))
 
while True:
    print "waiting for UDP data packet..."
    data, address = sock.recvfrom(256)
    print "Received packet from", address, "with data",data
    print "Sending  packet back to client"
    sock.sendto(data, address)
