class Obj(object):
  def __init__ (self, d, s, num):
    self.d = d
    self.s = s
    self.num = num
  def __str__(self):
    return self.d + ',' + self.s + ',' + self.num
  def __repr__(self):
    return str(self.d) + ',' + str(self.s) + ',' + str(self.num)

def search(toSearch, matrix):
  for obj in matrix:
    if obj.s <= toSearch <= obj.s + obj.num:
      return obj.d+(toSearch - obj.s)
  return toSearch

input = open('aoc23/input/day5.txt').read().strip()
loop = []
seeds = []
matrix = []
for line in input.splitlines():
  if len(line) == 0:
    if len(loop)>0:
      matrix.append(loop)
      loop=[]
  elif "seeds:" in line:
    for splitted in line.split(':')[-1].split():
      seeds.append(int(splitted))
  elif "map" not in line:
    nums = line.split()
    loop.append(Obj(int(nums[0]), int(nums[1]), int(nums[2])))
if len(loop)>0:
  matrix.append(loop)

answer1 = 10000000000000
for inp in seeds:
  for m in matrix:
    inp = search(inp, m)
  answer1 = min(answer1, inp)
print (answer1)# 424490994

def remap(lo, hi, m):
  # Remap an interval (lo,hi) to a set of intervals m
  ans = []
  for map in m:
    end = map.s + map.num - 1
    D = map.d - map.s  # How much is this range shifted
    if end >= lo and map.s <= hi:
      ans.append((max(map.s, lo), min(end, hi), D))

  for i, interval in enumerate(ans):
    l, r, D = interval
    yield (l + D, r + D)
    if i < len(ans) - 1 and ans[i+1][0] > r + 1:
      yield (r + 1, ans[i+1][0] - 1)

  # End and start ranges can use some love
  if len(ans) == 0:
    yield (lo, hi)
    return

  if ans[0][0] != lo:
    yield (lo, ans[0][0] - 1)
  if ans[-1][1] != hi:
    yield (ans[-1][1] + 1, hi)

answer2 = 10000000000000
for i in range(0, len(seeds), 2):
  cur_intervals = [(seeds[i], seeds[i] + seeds[i+1] - 1)]
  new_intervals = []
  for m in matrix:
    for hi, lo in cur_intervals:
      for new_interval in remap(hi, lo, m):
        new_intervals.append(new_interval)
    
    cur_intervals, new_intervals = new_intervals, []
  for lo, hi in cur_intervals:
    if lo>0:
      answer2 = min(answer2, lo)
print (answer2)