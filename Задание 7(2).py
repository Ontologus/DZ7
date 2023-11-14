list1 = input().split()
nlist1 = map(int, list1)
multiplicity = list(filter(lambda num:num % 19 == 0 or num % 13 == 0, nlist1))
print(multiplicity)