import time
import random
import socket

UDP_IP = "192.168.1.176" #IP address of your PC
UDP_PORT =  9999

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
while True:
 try:      
    value = 'wtf'  
    print(value)
    sock.sendto(value, (UDP_IP, UDP_PORT))
    print(sock.recv(1024).decode('utf-8'))
    # Sleep for half a second.
    time.sleep(0.5)
 except KeyboardInterrupt:
    break
print('\nStopped fine!')
