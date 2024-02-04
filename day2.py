import re

input = open('input/day2.txt').read().strip()
sum = 0
actual = {'red': 12, 'green': 13, 'blue': 14}
for line in input.splitlines():
  gameId = int(re.search("Game (\d*):.*", line).group(1))
  rounds = line.split(':')[1]
  exceeded = False
  max = {'red': -1, 'green': -1, 'blue': -1}
  for r in rounds.split(';'):
    for c in r.split(','):
      c = c.strip()
      n,color = c.split()
      if int(n) > max[color]:
        max[color] = int(n)
      # if int(n) > actual[color]:
      #   exceeded = True
      #   break;

  
  sum += max['red']*max['green']*max['blue']
  # if not exceeded:
  #   sum+=gameId

print (sum)