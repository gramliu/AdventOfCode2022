lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break

global_size = 0
MAX_SIZE = 100000


class Directory:
    def __init__(self, name: str, parent: 'Directory'):
        self.parent = parent
        self.name = name
        self.dirs = {}
        self.files = {}
        self.size = 0

    def add_dir(self, dir: str):
        self.dirs[dir] = Directory(dir, self)

    def get_dirs(self):
        return self.dirs

    def add_file(self, file: str, size: int):
        self.files[file] = size
        self.size += size

    def get_dir(self, dir: str):
        if dir == "..":
            return self.parent
        return self.dirs[dir]

    def get_size(self):
        global global_size, MAX_SIZE
        size = 0
        for dir in self.dirs.values():
            size += dir.get_size()
        size += self.size

        if size <= MAX_SIZE:
            global_size += size
        return size


dir = Directory("/", None)
for line in lines[1:]:
    tokens = line.split(" ")
    if tokens[0] == "$":
        cmd = tokens[1]
        if cmd == "ls":
            continue
        elif cmd == "cd":
            dir = dir.get_dir(tokens[2])
    elif tokens[0] == "dir":
        dir.add_dir(tokens[1])
    else:
        size = int(tokens[0])
        fname = tokens[1]
        dir.add_file(fname, size)

while dir.parent != None:
    dir = dir.parent

dir.get_size()
print(global_size)
