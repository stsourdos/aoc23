import re

input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
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