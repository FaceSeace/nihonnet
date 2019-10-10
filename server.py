import socket
import re
import pymysql
import time
import random
from socket import SOL_SOCKET,SO_REUSEADDR

#连接数据库
db = pymysql.connect("localhost", "root", "KID1412", "name")
cursor = db.cursor()
#正则
name="(?<='name': ').+?(?=', 'total')"
total="(?<='total': ).+?(?=, 'correct')"
correct="(?<='correct': ).+?(?=, 'accuracy')"
accuracy="(?<='accuracy': ).+?(?=})"
name = re.compile(name)
total = re.compile(total)
correct = re.compile(correct)
accuracy = re.compile(accuracy)

sk = socket.socket()
sk.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
sk.bind((socket.gethostname(), 4869))  #把地址绑定到套接字
print("启动成功")
print("=" * 30)
while True:
    sk.listen()          #监听链接
    conn, addr = sk.accept() #接受客户端链接
    ret = conn.recv(1024)  #接收客户端信息
    print("[",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"]", "\n",conn,'\n',addr)
    ret = str(ret.decode('utf-8'))
    try:
        username = re.search(name, ret).group()
        username = str(username)
        username = '"'+username+'"'
        usertotal = re.search(total, ret).group()
        usertotal = int(usertotal)
        usercorrect = re.search(correct, ret).group()
        usercorrect = int(usercorrect)
        useraccuracy = re.search(accuracy, ret).group()
        useraccuracy = float(useraccuracy)
        userid = str(int(time.time()))+str(random.randint(1000, 9999))
    except:
        print('用户输入数据非法')
        conn.close()
        continue
    sql = "insert into userdata (name, total, correct, accuracy, id) values (%s,%d,%d,%.2f,%s)" % (username, usertotal, usercorrect, useraccuracy, userid)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print(sql, "添加失败")
    print("【",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"】" ,ret)
    print("新数据: ",username, usertotal, usercorrect, useraccuracy)
    sql = "SELECT name, total,correct,accuracy,id FROM userdata ORDER BY correct DESC, accuracy DESC;"
    cursor.execute(sql)
    res = cursor.fetchall()
    db.commit()
    print("当前第一名: ", res[0])
    rank = ""
    list = []
    for i in res:
        list.append(i[-1])
    rank += str(list.index(userid) + 1) + " "
    rank += "李昌昊帅啊！！！2333"
    for i in res[0:10]:
        for j in i[0:-1]:
            rank += str(j) + " "
        rank = rank[:-1]
        rank += "李昌昊帅啊！！！2333"
    #打印客户端信息
    conn.send(rank.encode('utf-8'))        #向客户端发送信息
    conn.close()       #关闭客户端套接字