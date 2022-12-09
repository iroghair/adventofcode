class Dir:
    def __init__(self, name, parent=None):
        """Construct a Dir object that can contain files and subdirectories. 

        The self object is referred to as $PWD
        """
        self.name = name
        self.subdirs = list()
        self.files = list()
        self.parent = parent
        self.current_size = 0  # Total size of files in the local directory
        self.subdir_size = 0  # Total size of files in the local directory and recursive subdirs

    def __str__(self):
        return self.name

    # Add a new subdirectory with a unique name, return a reference
    def add_dir(self, name):
        """Add a subdirectory to $PWD, if a subdir with that name does not yet exist."""
        if (name not in self.get_sub_dir_names()):
            new_dir = Dir(name, self)
            self.subdirs.append(new_dir)
            print('Adding dir '+name)
            return self.subdirs[-1]
        return self.get_dir(name)

    def get_dir(self, name):
        """Return a reference to a directory object with a particular name 

        The directory should exist in the $PWD, otherwise None is returned
        """
        a = [dir for dir in self.subdirs if dir.get_dir_name() == name]
        return a[0]

    def add_file(self, name, size):
        """Add a file contained by $PWD, and append the size to the total directory size."""
        if (name not in self.get_sub_file_names()):
            print('Adding file: ', name, ' size: ', size)
            new_file = File(name, size)
            self.files.append(new_file)
            self.current_size = self.current_size + size
            self.update_parent_size(size)

    def update_parent_size(self, size):
        """Update the size of all parent folders."""
        self.subdir_size += size
        if(self.parent):
            self.parent.update_parent_size(size)
        return

    def get_dir_name(self):
        return self.name

    def get_sub_dir_names(self):
        """ Return the names of all the subdirectories in the $PWD """
        return [dir.get_dir_name() for dir in self.subdirs]

    def get_sub_file_names(self):
        return [file.get_file_name() for file in self.files]

    def get_current_size(self):
        """Return the size of all files in $PWD excluding those in subfolders."""
        return sum([file.get_file_size() for file in self.files])

    def get_subdir_size(self):
        """Return the size of all files in $PWD, including those in subfolders."""
        # Get the dirsize incl subdirs
        subdir_size = [dir.get_subdir_size()
                       for dir in self.get_recursive_subdirs()]
        out_list = list([self.name, subdir_size + self.get_current_size()])
        # out_list.append()
        return out_list

    def get_subdir_size2(self):
        """Return the size of all files in $PWD, including those in subfolders."""

        this_subdir_size = list()

        # Loop over all recursive dirs, including $PWD
        for dir in self.get_recursive_subdirs():
            print('Adding for ', self, ':  ', dir, dir.get_current_size())
            this_subdir_size.append(dir.get_current_size())

        # If this is a non-leaf folder, add the sum of each subdir size and flatten
        self.subdir_size = sum(this_subdir_size)

        return self.subdir_size

    def get_recursive_subdirs(self):
        """Return a list of the current and all recursively underlying subdir objects."""
        # Add the $PWD to the list
        dir_list = [self]

        # If this is a non-leaf folder, recurse into each subdir and flatten
        [[dir_list.append(subdir) for subdir in dir.get_recursive_subdirs()]
         for dir in self.subdirs if self.subdirs]

        return dir_list

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return self.name

    def get_file_name(self):
        return self.name

    def get_file_size(self):
        return int(self.size)


def build_tree(lines):
    """Build a directory/file tree based on terminal history and return the head node."""
    head_node = Dir('/')
    dir_list = [head_node]
    for line in [line.split() for line in lines]:
        if line[0] == 'cd':
            if line[1] == '/':
                present_working_dir = head_node
            elif line[1] == '..':
                present_working_dir = present_working_dir.parent
            else:
                present_working_dir = present_working_dir.add_dir(line[1])
                dir_list.append(present_working_dir)
        elif line[0] == 'ls':
            for n in range(1, len(line[1:]), 2):    # Remove the ls command
                if line[n] == 'dir':
                    present_working_dir.add_dir(line[n+1])
                elif line[n].isnumeric():
                    size = int(line[n])
                    name = line[n+1]
                    present_working_dir.add_file(name, size)

    return head_node, dir_list


if (False):
    head_node = Dir('/')
    head_node.add_dir('test')
    head_node.add_dir('test2')
    head_node.add_dir('test')
    head_node.add_file('myfile.txt', 738)
    dir = head_node.get_dir('test2')
    print(head_node.get_sub_dir_names())
else:
    myfile = 'input.txt'

    with open(myfile, 'r') as file:
        lines = [line for line in file.read().split('$') if line]

    head_node, dir_list= build_tree(lines)

    small_dir_sizes = [dir.subdir_size for dir in dir_list if (dir.subdir_size <= 100000)]
    print(sum(small_dir_sizes))
    headnode_size = head_node.subdir_size
    print(f'Total space: 70000000; Used space: {headnode_size:d}; Free space: {int(7e7-headnode_size)}')
    candidate_for_delete_sizes = [dir.subdir_size for dir in dir_list if (dir.subdir_size >= 3e7-(7e7-headnode_size))]
    print(f'{len(candidate_for_delete_sizes)} candidates for deletion found! Smallest folder is {min(candidate_for_delete_sizes)} bytes.')
    