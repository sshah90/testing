#use of python datatype
a, b, c = 5,3.5 , "Hello"
print('hello'+'smit')
print(3*1**3)
print("a is %r, b is %r, c is %r" %(type(a),type(b),type(c)))
print("a+b is  ",(a+b))
print("c[0:2] = ", c[:2])
e=['a', 1, 2, 3.5, 'Hello wolrd',7,15,17,25]
print("e is ", type(e))
print(22%3)

print("e[2] = ", e[2])
print("e[0:5] = ", e[0:5])
print("e[5:] = ", e[5:])
e.append(3)
print(e)
f=('a', 1, 2, 3.5, 'Hello wolrd',7)
#f.append(5)  any change in tuple will give error
print("f is ",type(f))

g = {1,3}
print("g is ",type(g))
g.add(2)
print(g)
g.update([2,3,4])
print(g)

h= {1:'value','key':2}
print("h is ",type(h))

print("h[1] = ", h[1]);

print("h['key'] = ", h['key']);


s=10
t= 5

print(s==t+5)
print(t+5 is s )