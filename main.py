from itertools import permutations

numbers = '011'
numbers1 = '11'

perlist = list(map(''.join,permutations(list(numbers),3)))

print(list(set(perlist)))

a=[]
a.append(int(numbers))
a.append(int(numbers1))
print(a)





