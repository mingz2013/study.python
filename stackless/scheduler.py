__author__ = 'tuyou'
'''
2.2 调度器(scheduler)
调度器控制各个微进程运行的顺序。如果刚刚建立了一组微进程，它们将按照建立的顺序来执行。在现实中，一般会建立一组可以再次被调度的微进程，好让每个都有轮次机会。一个快速演示:
'''

import stackless

def print_three_times(x):
    print "1:", x
    stackless.schedule()
    print "2:", x
    stackless.schedule()
    print "3:", x
    stackless.schedule()

stackless.tasklet(print_three_times)('first')

stackless.tasklet(print_three_times)('second')

stackless.tasklet(print_three_times)('third')

stackless.run()

'''
注意：当调用 stackless.schedule() 的时候，当前活动微进程将暂停执行，并将自身重新插入到调度器队列的末尾，好让下一个微进程被执行。
一旦在它前面的所有其他微进程都运行过了，它将从上次 停止的地方继续开始运行。这个过程会持续，直到所有的活动微进程都完成了运行过程。
这就是使用stackless达到合作式多任务的方式。
'''