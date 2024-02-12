input = open('aoc23/input/day9.txt').read().strip()

arr = [[int(c) for c in line.split()] for line in input.splitlines()]
def method(nums, part1):
  lst = list()
  for i in range(1, len(nums)):
    lst.append(nums[i] - nums[i - 1])
  zeros = [num for num in lst if num == 0]
  if len(zeros) == len(lst):
    return 0
  val = method(lst, part1)
  return val + lst[-1] if part1 else lst[0] - val

answer1 = 0
answer2 = 0
for history in arr:
  answer1 += method(history, True) + history[-1]
  answer2 += history[0] - method(history, False)
print(answer1)
print(answer2)