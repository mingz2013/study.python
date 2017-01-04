'''
Created on 2013-6-25

@author: root
'''
import tkinter
import time

if __name__ == '__main__':
    pass

curtime = ''
clock = tkinter.Label()
clock.pack()

def tick():
    global curtime
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clock.config(text = curtime)
    clock.after(200, tick)
tick()
clock.mainloop()
