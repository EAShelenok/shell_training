import io
from pprint import pprint

name = 'sample.txt'
file = open(name, 'r')
#print(file)
pprint(file.read())
file.close()

name = 'sample2.txt'
file1 = open(name, 'w')
file1.write('Hello')
file1.close()

name = 'sample2.txt'
file2 = open(name, 'a')
file2.write('world!')
file2.close()
