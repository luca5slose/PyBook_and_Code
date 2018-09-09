import socket
import time
#用TCP&IPV4
def sever_tcp():

    #第一个参数表示ipv4，第二个表示TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定本机和10086端口
    addr = ('127.0.0.1', 10010)
    sock.bind(addr)

    #tcp因为要先建立连接通道才能进行数据交流，所以需要监听
    sock.listen()

    while True:
        #接收访问，建立通道，返回值也是tuple，前一个是进行信息交流的本次通道用的socket，后者是地址
        skt, addr1 = sock.accept()
        #和UDP用的方法不一样
        data = skt.recv(500)

        msg = data.decode()

        print("收到来自{1}的以下内容：{0}".format(msg, addr1))

        #可选的反馈
        skt.send("Got it".encode())

        #用完通道要关闭,用的时候尽量增加通道的信息传输效率吧
        skt.close()

if __name__ == '__main__':
    print("starting tcp server*********")
    sever_tcp()
    print("ending tcp server***********")