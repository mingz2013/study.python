re = iter(range(5))

try:
    for i in range(100):
        print re.next()
except StopIteration:
    print 'here is end', i

print 'hahahahahaha'

