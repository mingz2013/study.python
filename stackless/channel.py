__author__ = 'tuyou'
'''
通道使得微进程之间的信息传递成为可能。它做到了两件事：
1.	能够在微进程之间交换信息。
2.	能够控制运行的流程。
又一个快速演示:

'''

import stackless

channel = stackless.channel()

def receiving_tasklet():
    print "Receiving tasklet started"
    print channel.receive()
    print "Receiving tasklet finished"

def sending_tasklet():
    print "Sending tasklet started"
    channel.send("send from sending tasklet")
    print "sending tasklet finished"

def another_tasklet():
    print "just another tasklet in the scheduler"

stackless.tasklet(receiving_tasklet)()

stackless.tasklet(sending_tasklet)()

stackless.tasklet(another_tasklet)()

stackless.run()
'''
接收的微进程调用 channel.receive() 的时候，便阻塞住，这意味着该微进程暂停执行，直到有信息从这个通道送过来。除了往这个通道发送信息以外，没有其他任何方式可以让这个微进程恢复运行。
若有其他微进程向这个通道发送了信息，则不管当前的调度到了哪里，这个接收的微进程都立即恢复执行；而发送信息的微进程则被转移到调度列表的末尾，就像调用了 stackless.schedule() 一样。

'''

'''
同样注意，发送信息的时候，若当时没有微进程正在这个通道上接收，也会使当前微进程阻塞
'''
