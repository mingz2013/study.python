func = lambda x,y:x + y
print func(3, 4)

print '*****************************'

def test(f, a, b):
    print 'test'
    print f(a, b)


test(func, 2, 3)

