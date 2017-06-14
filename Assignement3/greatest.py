# solution 5,6,8,9
from random import shuffle
lst=[]
for i in range(2000,3001):
    if i%5==0:
        lst.append(i)

print("Total numbers that can be dived by 5 in this range is :- %d"%(len(lst)))
print(lst)
print("Let's shuffle this list...")
print('-'*25)
shuffle(lst)
print("Now list looks like following..")
print(lst)
print("Let's find greatest element")
print('-'*25)
print("Largest element is",max(lst))
print("After sorting...")
print(sorted(lst))

word = 'abcdefghij'
print (word[:3] + word[3:])