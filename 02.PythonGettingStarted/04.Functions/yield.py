names = []

def save_name(name):
    f = open('resources/students.txt', 'a')
    f.write(f'{name}\n')
    f.close()

def load_names():
    f = open('resources/students.txt', 'r')
    for line in read_line(f):
        names.append(line)

def read_line(f):
    for line in f:
        yield line

save_name('Rahul')
save_name('Vijay')

load_names()

print(names)