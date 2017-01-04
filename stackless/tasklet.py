__author__ = 'tuyou'

import stackless

'''
2.1 微进程(tasklet)
微进程是stackless的基本构成单元，你可以通过提供任一个Python可调用对象（通常为函数或类的方法）来建立它，这将建立一个微进程并将其添加到调度器。这是一个快速演示:
'''

def print_x(x):
    print x

stackless.tasklet(print_x)('one')

stackless.tasklet(print_x)('two')

stackless.tasklet(print_x)('three')

# 注意，微进程将排起队来，并不运行，直到调用 stackless.run()
stackless.run()
