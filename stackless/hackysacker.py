__author__ = 'tuyou'
import thread
import random
import sys
import Queue
''''
一个“玩者”类的初始化用到了其名字，和一个指向包含了所有玩者的全局列表 circle 的引用，还有一个继承自Python标准库中的Queue类的消息队列。
Queue这个类的作用，与stackless的通道类似。它包含 put() 和 get() 方法，在一个空的Queue上调用 put() 会阻塞，直到另一个线程调用 put() 将数据送入Queue中为止。Queue这个类被设计为能与操作系统级的线程高效合作。
__init__ 方法接下来使用Python标准库中的thread模块新建一个线程，并在新线程中开始了一个消息循环。此消息循环是个无限循环，不停地处理队列中的消息。如果其收到一个特殊的消息 ‘exit’ ，则结束这个线程。
如果收到了另一个消息——指定其收到了沙包，玩者则从圈中随机选取一个其他玩者，通过向其发送一条消息来指定，将沙包再踢给它。
由类成员变量 hackysacker.counter 进行计数，当沙包被踢够了指定的次数时，将会向圈中的所有玩者都发送一条特殊的 ‘exit’ 消息。
注意，当全局变量debug为非零的时候，还有个函数debugPrint可以输出信息。我们可以使这游戏输出到标准输出，但当计时的时候，这会影响精确度。
一个“玩者”类的初始化用到了其名字，和一个指向包含了所有玩者的全局列表 circle 的引用，还有一个继承自Python标准库中的Queue类的消息队列。
Queue这个类的作用，与stackless的通道类似。它包含 put() 和 get() 方法，在一个空的Queue上调用 put() 会阻塞，直到另一个线程调用 put() 将数据送入Queue中为止。Queue这个类被设计为能与操作系统级的线程高效合作。
__init__ 方法接下来使用Python标准库中的thread模块新建一个线程，并在新线程中开始了一个消息循环。此消息循环是个无限循环，不停地处理队列中的消息。如果其收到一个特殊的消息 ‘exit’ ，则结束这个线程。
如果收到了另一个消息——指定其收到了沙包，玩者则从圈中随机选取一个其他玩者，通过向其发送一条消息来指定，将沙包再踢给它。
由类成员变量 hackysacker.counter 进行计数，当沙包被踢够了指定的次数时，将会向圈中的所有玩者都发送一条特殊的 ‘exit’ 消息。
注意，当全局变量debug为非零的时候，还有个函数debugPrint可以输出信息。我们可以使这游戏输出到标准输出，但当计时的时候，这会影响精确度。

'''
class hackysacker:
    counter = 0
    def __init__(self, name, circle):
        self.name = name
        self.circle = circle
        circle.append(self)
        self.messageQueue = Queue.Queue()

        thread.start_new_thread(self.messageLoop, ())

    def incrementCounter(self):
        hackysacker.counter += 1
        if hackysacker.counter >= turns:
            while self.circle:
                hs = self.circle.pop()
                if hs is not self:
                    hs.messageQueue.put('exit')

            sys.exit()

    def messageLoop(self):
        while 1:
            message = self.messageQueue.get()
            if message == "exit":
                debugPrint("%s is going home" % self.name)
                sys.exit()
            debugPrint("%s got hackeysack from %s" %(self.name, message.name))
            kickTo = self.circle[random.randint(0, len(self.circle) - 1)]
            debugPrint("%s kicking hackeysack to %s" %(self.name, kickTo.name))
            self.incrementCounter()
            kickTo.messageQueue.put(self)

def debugPrint(x):
    if debug:
        print(x)

debug = 1
hackysackers = 5
turns = 5

def runit(hs = 10, ts = 10, dbg = 1):
    global hackysackers, turns, debug
    hackysackers = hs
    turns = ts
    debug = dbg

    hackysacker.counter = 0
    circle = []
    one = hackysacker('1', circle)

    for i in range(hackysackers):
        hackysacker('1', circle)

    one.messageQueue.put(one)

    try:
        while circle:
            pass
    except:
        # 有时候我们在清理过程中会遇到诡异的错误
        pass

if __name__ == "__main__":
    runit(dbg=1)