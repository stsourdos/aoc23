input = open('input/day4.txt').read().strip()

answer1 = 0
scratch_hold = [1]*len(input.splitlines())
for i,line in enumerate(input.splitlines()):
  # part 1
  game = line.split(':')[-1].strip();
  winning = game.split('|')[0].split()
  selected = game.split('|')[-1].split()
  res = 0
  for select in selected:
    if select in winning:
      res = 1 if res == 0 else res * 2
  answer1 += res

  # part 2
  for duplis in range(0, scratch_hold[i]):
    wins = 0
    for select in selected:
      if select in winning and len(scratch_hold) > i + wins + 1:
        wins += 1
        scratch_hold[i+wins] += 1 

print (answer1)
print (sum(scratch_hold))