lines = []
with open('4/input.txt') as f:
    lines = f.

pairs = [line.strip().split(',') for line in lines]

pairs = [[elf.split('-') for elf in pair] for pair in pairs]

count = 0

print(len(pairs))

for pair in pairs:
    elf1 = pair[0]
    elf2 = pair[1]
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        count += 1

    elif int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
        count += 1

print(count)

count = 0

for pair in pairs:
    elf1 = set(range(int(pair[0][0]),int(pair[0][1]) + 1))
    elf2 = set(range(int(pair[1][0]),int(pair[1][1]) + 1))
    if elf1.intersection(elf2):
        count += 1

print(count)
