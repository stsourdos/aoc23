input = open('aoc23/input/day10.txt').read().strip()

arr = [[c for c in line] for line in input.splitlines()]
S = (0, 0)
for i, a in enumerate(arr):
  for y, b in enumerate(a):
    if b == 'S':
      S = (i, y)

queue = [S]
visited = set()
X_MAX = len(arr)
Y_MAX = len(arr[0])
while len(queue) > 0:
  pos = queue.pop(0)
  if pos not in visited:
    visited.add(pos)
    curr = arr[pos[0]][pos[1]]
    if pos[0] > 0 and (curr == 'S' or curr == '|' or curr=='L' or curr == 'J'):
      up = arr[pos[0] - 1][pos[1]]
      if up == '|' or up == '7' or up == 'F':
        queue.append((pos[0] - 1, pos[1]))
    if pos[0] < X_MAX - 1 and (curr == 'S' or curr == '|' or curr=='7' or curr == 'F'):
      down = arr[pos[0] + 1][pos[1]]
      if down == '|' or down == 'J' or down == 'L':
        queue.append((pos[0] + 1, pos[1]))
    if pos[1] > 0 and (curr == 'S' or curr == '-' or curr=='7' or curr == 'J'):
      left = arr[pos[0]][pos[1] - 1]
      if left == '-' or left == 'L' or left == 'F':
        queue.append((pos[0], pos[1] - 1))
    if pos[1] < Y_MAX - 1 and (curr == 'S' or curr == '-' or curr=='F' or curr == 'L'):
      right = arr[pos[0]][pos[1] + 1]
      if right == '-' or right == 'J' or right == '7':
        queue.append((pos[0], pos[1] + 1))
print(len(visited)/2)

tiles = 0
for i in range(0, X_MAX):
  in_loop = False
  tmp = 0
  for j in range(0, Y_MAX):
    if (i,j) in visited:
      in_loop = not in_loop
      if not in_loop:
        tiles += tmp
        tmp = 0
    elif in_loop:
      tmp += 1
print(tiles)# 502 too high