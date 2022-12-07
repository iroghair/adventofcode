from dataclasses import dataclass

# @dataclass


class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.subdirs = list()
        self.files = list()
        self.parent = parent

    def __str__(self):
        return self.name

    # Add a new subdirectory with a unique name, return a reference
    def add_dir(self, name):
        if (name not in self.get_sub_dir_names()):
            new_dir = Dir(name, self)
            self.subdirs.append(new_dir)
            return self.subdirs[-1]
        return self.get_dir(name)

    # Return a reference to a subdirectory with name
    def get_dir(self, name):
            a = [dir for dir in self.subdirs if dir.get_dir_name() == name]
            return a[0]

    def add_file(self, name, size):
        if (name not in self.get_sub_file_names()):
            new_file = File(name, size)
            self.files.append(new_file)

    def get_dir_name(self):
        return self.name

    def get_sub_dir_names(self):
        return [dir.get_dir_name() for dir in self.subdirs]

    def get_sub_file_names(self):
        return [file.get_file_name() for file in self.files]


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return self.name

    def get_file_name(self):
        return self.name


head_node = Dir('/')


if (False):

    head_node = Dir('/')

    head_node.add_dir('test')
    head_node.add_dir('test2')
    head_node.add_dir('test')
    head_node.add_file('myfile.txt', 738)
    dir = head_node.get_dir('test2')

    print(head_node.get_sub_dir_names())

else:
    myfile = 'test.txt'

    with open(myfile, 'r') as file:
        lines = [line for line in file.read().split('$') if line]

    # Build tree
    for line in [line.split() for line in lines]:
        if line[0] == 'cd':
            if line[1] == '/':
                current_dir = head_node
            elif line[1] == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.add_dir(line[1])
        elif line[0] == 'ls':
            for n in range(1,len(line[1:]),2): # Remove the ls command
                if line[n] == 'dir':
                    current_dir.add_dir(line[n+1])
                elif line[n].isnumeric():
                    size = int(line[n])
                    name = line[n+1]
                    current_dir.add_file(name,size)
