lines = []
with open('5/input.txt') as f:
    lines = f.readlines()

crates = lines[:8]
moves = lines[10:]

crates_arrays = [[], [], [], [], [], [], [], [], []]
for line in crates:
    for i in range(1, 35, 4):
        if line[i] != " ":
            crates_arrays[int(i/4)] = [line[i]] + crates_arrays[int(i/4)]


for line in moves:
    line = line.split()
    move = int(line[1])
    from_ = int(line[3])-1
    to = int(line[5])-1
    
    # PART 1
    # for i in range(0, move):
    #     popped = crates_arrays[from_].pop()
    #     crates_arrays[to].append(popped)

    # PART 2
    from_array = crates_arrays[from_]
    to_move = from_array[-move:]
    crates_arrays[from_] = from_array[:len(from_array)-move]
    crates_arrays[to] = crates_arrays[to] + to_move

msg = [stack[-1] for stack in crates_arrays]
print("".join(msg))
