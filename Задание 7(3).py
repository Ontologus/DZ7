from functools import reduce
list1 = input().split()
nlist1 = map(int, list1)
def maximum(nlist1):
  return reduce(lambda x, y: x if x > y else y, nlist1)
print(maximum(nlist1))