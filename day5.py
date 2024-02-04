input="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

"""


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
      diff = toSearch - obj.s
      return obj.d+diff
  return toSearch

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

answer1 = 10000000000000
for i in range(0, len(seeds), 2):
  print (i)
  for inp in range(seeds[i], seeds[i]+seeds[i+1]):
    for m in matrix:
      inp = search(inp, m)
    answer1 = min(answer1, inp)

print (answer1)# 424490994