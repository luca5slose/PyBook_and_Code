import socket

def clientTest():
    #TCP参数是socket.SOCK_STREAM
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "喂喂喂！！！收的到吗？"

    data = text.encode()
    sock.sendto(data, ("127.0.0.1", 10086))

    rcvdata, addr = sock.recvfrom(300)
    print("??????????你不走了？")
    rcvtext = rcvdata.decode()
    print(rcvtext)

if __name__ == '__main__':
    clientTest()