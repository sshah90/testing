the_count = [1,2,3,4,5,6]
fruits = ['apples','orange','pears','banana']
change = [1,'pennies',2,'dimes',3,'quarters']
#this is list

for numbers in the_count:
    print "this is count %d" %numbers
	
for fruit in fruits:
    print "A fruit of type:%s" %fruit
	
for i in change:
    print "i got %r" %i

elements=[]

for i in range(0,6):
    print "Adding %d to the list" %i 
    elements.append(i)
	
for i in elements:
    print "element was : %d" %i