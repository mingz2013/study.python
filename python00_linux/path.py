import os.path

path = '/media/mingzz/disk1/studymyself/python/file.txt'

print(os.path.basename(path))

print(os.path.dirname(path))

info = os.path.split(path)
print(info)
path2 = os.path.join('/','media','mingzz','disk1','studymyself','python','file1.txt')

p_list = [path, path2]

print(os.path.commonprefix(p_list))


print('--------------------------------------')

print(os.path.exists(path))
print(os.path.getsize(path))
print(os.path.getatime(path))
print(os.path.getmtime(path))

print(os.path.isfile(path))
print(os.path.isdir(path))



