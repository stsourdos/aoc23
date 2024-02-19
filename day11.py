input = open('aoc23/input/day11.txt').read().strip()

arr = [[c for c in line] for line in input.splitlines()]

galaxies = list()
for i, a in enumerate(arr):
  for j, b in enumerate(a):
    if b == '#':
      galaxies.append((i,j))

rows_extended = set()
for i, line in enumerate(input.splitlines()):
  if '#' not in line:
    rows_extended.add(i)

cols_extended = set()
for j in range(len(arr[0])):
  line = ''
  for i in range(len(arr)):
    line += arr[i][j]
  if '#' not in line:
    cols_extended.add(j)

def manhattan(gal1, gal2):
  return abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])

answer1 = 0
answer2 = 0
for i, gal1 in enumerate(galaxies):
  for j in range(i+1, len(galaxies)):
    gal2 = galaxies.__getitem__(j)
    answer1 += manhattan(gal1, gal2)
    answer2 += manhattan(gal1, gal2)
    for row in range(gal1[0], gal2[0]):
      if row in rows_extended:
        answer1 += 1
        answer2 += 999999
    step = 1 if gal1[1] < gal2[1] else -1
    for col in range(gal1[1], gal2[1], step):
      if col in cols_extended:
        answer1 += 1
        answer2 += 999999
print (answer1)
print (answer2)