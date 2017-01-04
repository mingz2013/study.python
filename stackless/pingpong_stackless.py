__author__ = 'tuyou'
import stackless

ping_channel = stackless.channel()
pong_channel = stackless.channel()

def ping():
    while ping_channel.receive(): # 在此阻塞
        print("PING")
        pong_channel.send("from ping")

def pong():
    while pong_channel.receive():
        print("PONG")
        ping_channel.send("from pong")

stackless.tasklet(ping)()
stackless.tasklet(pong)()

# 我们需要发送一个消息来初始化这个游戏的状态
# 否则，两个微进程都会阻塞
stackless.tasklet(ping_channel.send)('startup haha')

stackless.run()