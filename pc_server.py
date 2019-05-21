import socket, traceback

host = '192.168.1.200'
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.1.200', 9999))
while 1:
    try:
        message, address = srecvfrom(64)
        if message == "":break
        print"Got data from", address
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
        
