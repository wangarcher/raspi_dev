import socket


UDP_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.1.200',UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print "received message:", data
    reply = 'Hello,%s!'  % data.decode('utf-8')
    sock.sendto(reply.encode('utf-8'),addr)
