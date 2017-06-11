from sys import argv

script,filename = argv

print "we r going to erase %r"  %filename
print "If you don't want that,hit CTRL-C"
print "If you want that,hit return"

raw_input("?")

print "openning the file..."

target =open (filename,'w')

print "truncating the file  GoodBye..!!"

target.truncate()

print "now i am going to ask u for three line"

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")



print "and finally,we close it"
target.close()

