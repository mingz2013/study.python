import time

print(time.time())
print(time.clock())

print('start')
time.sleep(10)
print('wake up')

st = time.gmtime()
print(st)
st = time.localtime()
print(st)
s = time.mktime(st)
print(s)

