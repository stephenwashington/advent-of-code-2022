from logging import root


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirectories = []
        self.files = []
        self.size = 0

    def __repr__(self):
        return self.name


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return self.name

def find_subdirectory(parent_directory, subdirectory_name):
    directory = None
    for d in parent_directory.subdirectories:
        if d.name == subdirectory_name:
            directory = d
            break
    return directory

size = 0
def get_size_less_than_100k(directory):
    global size
    total_size = 0
    for f in directory.files:
        total_size += f.size
    for d in directory.subdirectories:
        total_size += get_size_less_than_100k(d)
    if total_size <= 100000:
        size += total_size
    directory.size = total_size
    if total_size > 6090134: # part 2
        print(directory.name, total_size)
    return total_size

with open("input.txt") as f:
    root_directory = Directory("/", None)
    current_directory = root_directory
    parent_name = "/"
    reading_files = False
    for line in f:
        l = line.strip().split()
        if l[0] == "$":
            command = l[1]
            if command == "cd":
                reading_files = False
                argument = l[2]
                if argument == "..":
                    current_directory = current_directory.parent
                elif argument == "/":
                    current_directory = root_directory
                else:
                    current_directory = find_subdirectory(current_directory, argument)
            elif command == "ls":
                reading_files = True
        else:
            try:
                filesize = int(l[0])
                filename = l[1]
                new_file = File(filename, filesize)
                current_directory.files.append(new_file)
            except ValueError:
                directory_name = l[1]
                new_directory = Directory(l[1], current_directory)
                current_directory.subdirectories.append(new_directory)
    # Part 1: Combined size of all directories less than 100 000 in size
    get_size_less_than_100k(root_directory)
    print(size)
