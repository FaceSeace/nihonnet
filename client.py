import socket

sk = socket.socket()           # 创建客户套接字
sk.connect((socket.gethostname(), 4869))    # 尝试连接服务器
a = {'name':'2333',
     'score':0}
a = str(a)
sk.send(a.encode('utf-8'))
ret = sk.recv(1024)         # 对话(发送/接收)
print(ret)
sk.close()            # 关闭客户套接字