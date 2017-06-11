def add(a,b):
    print "ADDING %d+%d" %(a,b)
    return a+b

def subtract(a,b):
    print "Sub %d-%d" %(a,b)
    return a-b

def mul(a,b):
    print "mul %d*%d " %(a,b)
    return a*b

def div(a,b):
    print "Div %d/%d" %(a,b)
    return a/b
	
print "let's put some value on it"
x = add(30,5)
y = subtract(50,4)
z=mul(5,4)
v=div(20,5)

print "x=%d,y=%d,z=%d,v=%d" %(x,y,z,v)

what = add(x, subtract(y, mul(z, div(v, 2))))

print what 