import socket
import time
#用UDP&IPV4
def severTest():

    #第一个参数表示ipv4，第二个表示UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    addr = ('127.0.0.1', 10086)
    sock.bind(addr)
    #绑定本机和10086端口

    data, adr = sock.recvfrom(500)
    #接收信息，参数是缓冲区大小，信息格式是tuple，前一个数据，后一个地址
    #注意信息流是byte格式，收发都要编码,默认是UTF-8
    text = data.decode()
    print(text)

    #接收到之后还可以发送反馈，非强制
    rsp = "已经收到了"
    repdata = rsp.encode()
    sock.sendto(repdata, adr)

if __name__ == '__main__':
    print("starting server*********")
    while True:
        try:
            severTest()
        except Exception as e:
            print(e)
        time.sleep(1)