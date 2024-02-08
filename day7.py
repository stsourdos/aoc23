
from collections import Counter
import functools

class Play(object):
  def __init__ (self, cards, bid):
    self.cards = cards
    self.bid = int(bid)
  def __repr__(self):
    return self.cards + ', ' + str(self.bid) + ', ' + str(self.playtype())

  def playtype1(self, cards):
    key_to_freq = Counter(cards)
    jokers = key_to_freq.get('J', 0)
    key_to_freq = sorted(key_to_freq.items(), key=lambda item: item[1],reverse=True)
    res = 1
    if key_to_freq[0][1] == 5:
      res = 7
    elif key_to_freq[0][1] == 4:
      res = 6
    elif key_to_freq[0][1] == 3 and key_to_freq[1][1] == 2:
      res = 5
    elif key_to_freq[0][1] == 3 and key_to_freq[1][1] == 1:
      res = 4
    elif key_to_freq[0][1] == 2 and key_to_freq[1][1] == 2:
      res = 3
    elif key_to_freq[0][1] == 2 and key_to_freq[1] [1]== 1:
      res = 2
    #return res
    
    ## Part-2
    if jokers == 0 or res == 7:
      return res
    symbol = key_to_freq[1][0] if key_to_freq[0][0] == 'J' else key_to_freq[0][0]
    c = cards.replace('J', symbol)
    return self.playtype1(c)
  
  def playtype(self):
    return self.playtype1(self.cards)


def alphatonum(c):
  if c=='A': return 14
  if c=='K': return 13
  if c=='Q': return 12
  if c=='J': return 1## 11 ## Part-2
  if c=='T': return 10
  return -1

def compare(x, y):
  if x.playtype() > y.playtype():
    return 1
  elif x.playtype() < y.playtype():
    return -1
  else:
    for i in range(0, 5):
      xi = x.cards[i]
      yi = y.cards[i]
      if not xi.isdigit():
        xi = alphatonum(xi)
      if not yi.isdigit():
        yi = alphatonum(yi)
      xi=int(xi)
      yi=int(yi)
      if xi > yi:
        return 1
      if xi < yi:
        return -1
    return 0

input = open('aoc23/input/day7.txt').read().strip()
plays = []
for line in input.splitlines():
  plays.append(Play(line.split()[0],line.split()[1]))

p_sorted = sorted(plays, key=functools.cmp_to_key(compare))
answer = 0
for i,obj in enumerate(p_sorted):
  answer += (i+1) * obj.bid
print (answer)