
priorities = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

rucksacks = []
with open('3/rucksacks.txt') as f:
    rucksacks = f.readlines()
rucksacks = [rucksack.strip() for rucksack in rucksacks]
rucksacks = [[rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]] for rucksack in rucksacks]

score = 0

for rucksack in rucksacks:
    in_both = set()
    for item in rucksack[0]:
        if item in rucksack[1]:
            in_both.add(item)

    for item in in_both:
        score += priorities.index(item)

print(score)