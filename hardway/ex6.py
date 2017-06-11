x= "there are only %d type of people." %10
binary= "binary"
do_not = "don't"
y = "those who knows %s and those who %s" %(binary,do_not)

print x
print y

print "i said %r" %x
print "i aslo said: '%s'" %y


hilarious= False
joke = "oh! it's funny !! %r"

print joke%hilarious
w= "this is the left side of..."
e= "a string with a right side"

print w+e