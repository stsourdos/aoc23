import sys

def isspecial(c):
  return not c.isdigit() and not c=='.'

def hasSymbol(arr, i, y):
  if len(arr)>i+1 and isspecial(arr[i+1][y]):# down
    return True
  if i>0 and isspecial(arr[i-1][y]):# up
    return True
  if len(arr[0])>y+1 and isspecial(arr[i][y+1]):# right
    return True
  if y>0 and isspecial(arr[i][y-1]):# left
    return True
  if len(arr)>i+1 and len(arr[0])>y+1 and isspecial(arr[i+1][y+1]):# downright
    return True
  if i>0 and y>0 and isspecial(arr[i-1][y-1]):# upleft
    return True
  if len(arr)>i+1 and y>0 and isspecial(arr[i+1][y-1]):# downleft
    return True
  if i>0 and len(arr[0])>y+1 and isspecial(arr[i-1][y+1]):# upright
    return True
  return False

def getNum(result, arr, i, y):
  res = ''
  for x in range(y, len(arr[0])):
    if (arr[i][x].isdigit()):
      res = res + arr[i][x]
    else:
      break;

  for y in range(y-1, -1, -1):
    if (arr[i][y].isdigit()):
      res = arr[i][y] + res
    else:
      break;
  num=int(res)
  if num not in result:
    result.append(num)
  return result

def getNums(arr, i, y):
  res = []
  if len(arr)>i+1 and (arr[i+1][y]).isdigit():# down
    (getNum(res, arr, i+1, y))
  if i>0 and (arr[i-1][y]).isdigit():# up
    (getNum(res, arr, i-1, y))
  if len(arr[0])>y+1 and (arr[i][y+1]).isdigit():# right
    (getNum(res, arr, i, y+1))
  if y>0 and (arr[i][y-1]).isdigit():# left
    (getNum(res, arr, i, y-1))
  if len(arr)>i+1 and len(arr[0])>y+1 and (arr[i+1][y+1]).isdigit():# downright
    (getNum(res, arr, i+1, y+1))
  if i>0 and y>0 and (arr[i-1][y-1]).isdigit():# upleft
    (getNum(res, arr, i-1, y-1))
  if len(arr)>i+1 and y>0 and (arr[i+1][y-1]).isdigit():# downleft
    (getNum(res, arr, i+1, y-1))
  if i>0 and len(arr[0])>y+1 and (arr[i-1][y+1]).isdigit():# upright
    (getNum(res, arr, i-1, y+1))
  return res

input = open(sys.argv[1]).read().strip()
# rows, cols = (len(input.splitlines()), len(input.splitlines()[0]))
# arr = [[0 for i in range(cols)] for j in range(rows)]
# for i,line in enumerate(input.splitlines()):
#   for y,c in enumerate(line):
#     arr[i][y] = c

lines = input.splitlines()
arr = [[c for c in line] for line in lines]

# Part-1
sum = 0
for i,row in enumerate(arr):
  number = ''
  symbol_around = False
  for y,c in enumerate(row):
    if c.isdigit():
      number += c
      if hasSymbol(arr, i, y):
        symbol_around = True
      if y==len(arr[0])-1 and symbol_around:
        sum += int(number)
    else:
      if symbol_around and not number == '':
        sum += int(number)
      number = ''
      symbol_around = False

print (sum)# 539637

# Part-2
sum2 = 0
for i,row in enumerate(arr):
  for y,c in enumerate(row):
    if c=='*':
      nums = getNums(arr, i, y)
      if len(nums) == 2:
        sum2 += nums[0]*nums[1]

print(sum2)#82818007