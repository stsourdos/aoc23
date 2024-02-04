def execute(time, distance):
  count = 0
  answer = 1
  for i,t in enumerate(time):
    d = distance[i]
    for tx in range(1, t):
      time_left = t - tx
      if (time_left*tx) > d:
        count += 1
    answer *= count
    count = 0
  return answer

input = open('input/day6.txt').read().strip()

time = list(map( int, input.splitlines()[0].split(':')[-1].split()))
distance = list(map( int, input.splitlines()[1].split(':')[-1].split()))
print(execute(time, distance)) #Part-1

time = [int(input.splitlines()[0].split(':')[-1].replace(' ', ''))]
distance = [int(input.splitlines()[1].split(':')[-1].replace(' ', ''))]
print(execute(time, distance)) #Part-2