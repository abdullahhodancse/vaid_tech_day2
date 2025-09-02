numbers={1,2,3,4,2,1,11,4,5,6,7,120,11}

print(numbers)

numbers.add(300)
print(numbers)

numbers.remove(11) #number na thakle error dibe
print(numbers)

numbers.discard(90)# n umber na thakle o error dei na
print(numbers)

a={12,14,11,19,20,32,23}
b={11,12,13,18,19,20,21}

print(a.union(b)) 
print(a.intersection(b))
print(a.difference((b)))
print(a.symmetric_difference(b))