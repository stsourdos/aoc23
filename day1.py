input = open('input/day1.txt').read().strip()
sum = 0
for line in input.splitlines():
  line_list = [];
  for i,c in enumerate(line):
    if c.isdigit():
      line_list.append(c)
    for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
      if line[i:].startswith(val):
        line_list.append(str(d+1))
  #print (line_list)
  sum+=int(line_list[0]+line_list[-1])

print(sum)