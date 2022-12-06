
priorities = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

rucksacks = []
with open('3/rucksacks.txt') as f:
    rucksacks = f.readlines()
rucksacks = [rucksack.strip() for rucksack in rucksacks]


score = 0

for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    for item in set(group[0]):
        if item in group[1] and item in group[2]:
            score += priorities.index(item)

print(score)