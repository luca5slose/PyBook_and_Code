import socket

def client_tcp():
    #首先搞一个socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #建立连接
    addr = ("127.0.0.1", 10010)
    sock.connect(addr)

    #发送，方法也和UDP有点不一样
    text = "Can you hear me?"
    sock.send(text.encode())

    #接收反馈，可选
    rcv = sock.recv(500)
    print(rcv.decode())

if __name__ == '__main__':
    client_tcp()