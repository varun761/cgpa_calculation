file = open('./sample-data/sample.txt')
file_reader = file.read(18)
print(file_reader, end=' ')
file_reader = file.read(0)
if file_reader.isspace():
    print('is space', end=' ')
else:
    print('no')
file_reader = file.read(21)
print(file_reader, end=' ')
file.close()

# create new set
s = set([2,3,3,2,3,4])
print(s)

# dictionary
dic = {'name': 'Varun', 'course': {'cse': 1, 'btech': 1}}
print(type(dic))

#exe

file = open('./sample-data/DiscordSetup.exe', 'r+b')
file_reader = file.read(19)
print(type(file_reader))

#readline
file = open('./sample-data/sample.txt')
for lines in file:
    print(lines)
file.close()
