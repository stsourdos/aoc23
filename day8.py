import re

input = open('aoc23/input/day8.txt').read().strip()

directions = input.splitlines()[0]
map = dict()
a_nodes = []
for kv in input.splitlines():
  if '=' in kv:
    regex = re.search("(\w{3}) = \((\w{3}), (\w{3})\)", kv)
    map[regex.group(1)] = (regex.group(2), regex.group(3))
    if regex.group(1).endswith('A'):
      a_nodes.append(regex.group(1))

current = 'AAA'
pos = 0
answer1 = 0
while(current != 'ZZZ'):
  tpl = map[current]
  current = tpl[0] if directions[pos] == 'L' else tpl[1]
  answer1 += 1
  pos = 0 if len(directions) == pos + 1 else pos + 1
print (answer1)

pos = 0
answer2 = 0
while(True):
  for i,nd in enumerate(a_nodes):
    tpl = map[nd]
    a_nodes[i] = tpl[0] if directions[pos] == 'L' else tpl[1]
  pos = 0 if len(directions) == pos + 1 else pos + 1
  z_nodes = 0
  answer2 +=1
  for nd in a_nodes:
    if nd.endswith('Z'):
      z_nodes+=1
  if z_nodes == len(a_nodes):
    break
print(answer2)