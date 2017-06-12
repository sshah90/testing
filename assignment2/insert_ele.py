a=int(input("How many number you want to add? "))
print("Ok so you can add %d numbers in list" %a)

lst=[]
for i in range(1,a+1):
    b=int(input("give me %d number: " %i))
    lst.append(b)
    print("Now your list look like...")
    print(lst)
