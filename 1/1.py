
with open('1/calories.txt') as f:
    lines = f.read()


elves = lines.split('\n\n')

elves = [elf.split() for elf in elves]

elves = [sum([int(calories) for calories in elf]) for elf in elves]

print(max(elves))
elves.sort(reverse=True)
print(sum(elves[0:3]))
