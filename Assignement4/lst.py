lst=[1,2,3,4,5,6,7,5,4,5]
print("Before changing in list...",lst)
s=int(input("Give me integer :- "))
lst1=[]
for i in lst:
    lst1.append(i*s)

print("After multiplied by",s,"new list is...",lst1)

print("Removing duplicate ",set(lst))

print("First number is ",lst[0],"While last number is ",lst[-1])

s=str(input("Give me any string i will reverse it.. "))
print(s[::-1])