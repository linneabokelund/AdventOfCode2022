lines = []
with open('7/input.txt') as f:
    lines = f.readlines()

file_system = {"/": {}}
current_dir = ''
for line in lines:
    if line[0] == '$':
        cmd = line.split()[1:]
        if cmd[0] == "cd":
            if cmd[1] == "..":
                current_dir = "/".join(current_dir.split("/")[:-1])
            elif cmd[1] == "/":
                current_dir = "/"
            else:
                if current_dir == "/":
                    current_dir += cmd[1]
                else:
                    current_dir += "/" + cmd[1]
    else:
        children = file_system["/"]
        for dir in current_dir.split("/"):
            if dir:
                children = children[dir]
        if line.split()[0] == "dir":
            if not line.split()[1] in children.keys():
                children[line.split()[1]] = {}
        else:
            children[line.split()[1]] = line.split()[0]


sizes = []
i = 0
def get_children_size(children):
    size = 0
    for key, value in children.items():
        if isinstance(value, str):
            size += int(value)
        else:
            this_dirs_size = get_children_size(value)
            sizes.append(this_dirs_size)
            size += this_dirs_size
    return size

sizes.append(get_children_size(file_system["/"]))

#TASK 1
sizes_to_count = [value for value in sizes if value <= 100000]
print(sum(sizes_to_count))

#TASK 2
USED = max(sizes)
TOTAL = 70000000
FREE_NEED = 30000000
current_free_space = TOTAL-USED
min_delete = FREE_NEED-current_free_space

meet_min = [size for size in sizes if size >= min_delete]
print(min(meet_min))