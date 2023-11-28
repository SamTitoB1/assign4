import socket

target = '10.0.0.1'

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False


for port in range(1,100):
    result = portscan(port)
    if result:
        print('open')
    else:
        print('closed')
