import math
import re

input = open('aoc23/input/day8.txt').read().strip()
directions = input.splitlines()[0]
map = dict()
for kv in input.splitlines():
  if '=' in kv:
    regex = re.search("(\w{3}) = \((\w{3}), (\w{3})\)", kv)
    map[regex.group(1)] = (regex.group(2), regex.group(3))
a_nodes = [x for x in map if x[2] == 'A']

def walk(current):
  pos = 0
  answer = 0
  while(not current.endswith('Z')):
    tpl = map[current]
    current = tpl[0] if directions[pos] == 'L' else tpl[1]
    answer += 1
    pos = 0 if len(directions) == pos + 1 else pos + 1
  return answer

print (walk('AAA')) # part-1

answer2 = 1
for i,nd in enumerate(a_nodes):
  res = walk(nd)
  answer2 = math.lcm(answer2, res)
print (answer2) # part-2