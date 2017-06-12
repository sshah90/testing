a=int(input("Give me first num :- "))
b=int(input("Give me second num :- "))
c=int(input("Give me third num :- "))

if(a>b) and (a>c):
    print("%d is greater number than %d and %d" %(a,b,c))

elif (b>a) and (b>c):
    print("%d is greater number than %d and %d" % (b, a, c))

else:
    print("%d is greater number than %d and %d" % (c, a, b))
