#functions
def print__two(*args):
    arg1, arg2 = args
    print "arg1: %r,arg2: %r" % (arg1,arg2)

def print_again(arg1,arg2):
    print " arg1: %r,arg2: %r" %(arg1,arg2)
	
def print_none():
    print "i got nothing"

   
print__two("Smit","shah")
print_again("shah","smit")
print_none()