def func(a):
    if a > 100:
        return True
    else:
        return False
print filter(func, [10, 56, 101, 500])

