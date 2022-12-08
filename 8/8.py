lines = []
with open('8/input.txt') as f:
    lines = f.readlines()

map = []
for line in lines:
    map.append(line.strip())

def checkUp(m,n):
    my_height = map[m][n]
    for i in range(m-1, -1, -1):
        if my_height <= map[i][n]:
            return False, m-i
    return True, m

def checkDown(m,n):
    my_height = map[m][n]
    for i in range(m+1, len(map)):
        if my_height <= map[i][n]:
            return False, i-m
    return True, len(map)-m-1

def checkLeft(m,n):
    my_height = map[m][n]
    for j in range(n-1, -1, -1):
        if my_height <= map[m][j]:
            return False, n-j
    return True, n

def checkRight(m,n):
    my_height = map[m][n]
    for j in range(n+1, len(map)):
        if my_height <= map[m][j]:
            return False, j-n
    return True, len(map)-n-1


visable_trees = 0
scenic_scores = []

for i in range(0, len(map)):
    for j in range(0, len(map)):
        visableFromN, treesAbove = checkUp(i, j)
        visableFromS, treesBelow = checkDown(i, j)
        visableFromW, treesLeft = checkLeft(i, j)
        visableFromE, treesRight = checkRight(i, j)
        visable = (visableFromN or visableFromS or
                   visableFromW or visableFromE)
        if visable:
            visable_trees += 1
        scenic_score = treesAbove*treesBelow*treesLeft*treesRight
        scenic_scores.append(scenic_score)
        
print(visable_trees)
print(max(scenic_scores))