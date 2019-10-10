import random
import socket

lm = [
    'a','i','u','e','o',
    'ka','ki','ku','ke','ko',
    'sa','shi','su','se','so',
    'ta','chi','tsu','te','to',
    'na','ni','nu','ne','no',
    'ha','hi','fu','he','ho',
    'ma','mi','mu','me','mo',
    'ya','yu','yo',
    'ra','ri','ru','re','ro',
    'wa','o',
    'n'
    ]
ping = [
    'あ','い','う','え','お',
    'か','き','く','け','こ',
    'さ','し','す','せ','そ',
    'た','ち','つ','て','と',
    'な','に','ぬ','ね','の',
    'は','ひ','ふ','へ','ほ',
    'ま','み','む','め','も',
    'や','ゆ','よ',
    'ら','り','る','れ','ろ',
    'わ','を',
    'ん'
    ]
sk = socket.socket()
cnt = 0
acnt = 1
all = 0
name = ""
near = [-1] * 40
aim = ""

def initdata():
    global cnt, acnt, all, name, near, aim, sk
    cnt = 0
    acnt = 1
    all = 0
    name = ""
    near = [-1] * 40
    aim = ""
    sk = socket.socket()


def get_ans(aim):
    return lm[ping.index(aim)]


def getname_and_all(username ,allcnt):
    global name, all
    name = username
    all = allcnt
    if "'" in name or '"' in name or " " in name or name == "":
        name = "default"
        print("名字被重置为default")
    if all < 20:
        all = 20
        print("总次数被重置为:20次")


def title():
    global acnt, near, cnt, aim, all
    aim = random.choice(ping)
    while ping.index(aim) in near:
        aim = random.choice(ping)
    print(aim, end="")
    print(" " * 3, end="")
    print(acnt-cnt, "/", acnt)
    return [aim, acnt-cnt-1, acnt]

def judge(ans):
    print(ans)
    global acnt, near, cnt, aim
    print(acnt, all)
    acnt += 1
    if acnt % 40 == 0:
        near = [-1] * 40
    if ans == lm[ping.index(aim)]:
        near.pop(0)
        near.append(ping.index(aim))
        print("")
        return [True]
    else:
        cnt += 1
        print(lm[ping.index(aim)])
        print('*' * 10)
        print('错', cnt, '个')
        print('*' * 10)
        return [False, lm[ping.index(aim)], cnt]


def user_result_and_updata():
    remsg = []
    print('共', all, '个,对', all-cnt, '个，错', cnt, '个')
    l = ((all-cnt)/all)*100
    print('正确率%.2f%%' % l)
    remsg.append('共' + str(all) + '个,对' + str(acnt - cnt) + '个，错' + str(cnt) + '个')
    remsg.append('正确率%.2f%%' % l)
    msg = {'name': name,
           'total': all,
           'correct': all-cnt,
           'accuracy': l}
    try:
        sk.connect(('120.78.74.113', 4869)) #记得改地址
        msg = str(msg)
        sk.send(msg.encode('utf-8'))
        ret = -1
        ret = sk.recv(1024)
        ret = ret.decode('utf-8')
        ret = str(ret)
        rank = ret.split(" ", 1)[0]
        ret = ret.split(" ", 1)[1]
        listten = ret.split('李昌昊帅啊！！！2333')
        listten = listten[1:-1]
        i = 1
        print("%-16s%-16s%-16s%-16s%-16s" % ("名 次", "名 字", "测试量", "正确量", "正确率"))
        remsg.append(rank)
        for item in listten:
            a = "第%d位\t" % i
            a = str(a)
            temp = []
            print("%-16s" % a, end="")
            for info in item.split():
                print("%-16s" % info, end="")
                temp.append(str(info))
            i += 1
            print("")
            remsg.append(temp)
        print("你这回在第", rank, "名")
        sk.close()
        return remsg
    except:
        remsg.append(False)
        print('上传失败，请检查网络或名字不合法')
        return remsg