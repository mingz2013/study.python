f = open('file.txt', "r")

content = f.readline()

f.close()

print content

f = open('file.txt', "w")

f.write('I write a line')

f.close()

f = open('file.txt', "r")

content = f.readlines()

print content

f.close()


