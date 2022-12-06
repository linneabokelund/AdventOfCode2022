chars = []
with open('6/input.txt') as f:
    chars = f.read().strip()

# TASK 1
# NBR = 4

# TASK 2
NBR = 14

potential_marker = chars[:NBR-1]

for i in range(NBR-1, len(chars)):
    potential_marker += chars[i]
    if len(set(potential_marker)) == NBR:
        print(potential_marker)
        print(i+1)
        break
    potential_marker = potential_marker[1:]

