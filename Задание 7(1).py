list1 = input().split()
list2 = input().split()
summa = list(map(lambda x, y:x + y, list(map(int, list1)) + [0,] * (len(list2) - len(list1)), list(map(int, list2)) + [0,] * (len(list1) - len(list2))))
print(summa)