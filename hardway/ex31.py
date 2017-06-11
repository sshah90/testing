print "you enter a dark room with two doors. Do you through door #1 or door #2?"

door = raw_input(">")

if door == "1":
    print "There's a giant bear here eating a cheese cake. what do you do?"
    print "1.Take the cake."
    print "2. Screm at the bear"
   
    bear =raw_input(">")
    if bear== "1":
	    print "the bear eats yourface off. Good Job!"
	       
    elif bear == "2":
          print "the bears eats your legs off. Good Job!"
	
    else :
        print "well,doing %s is probaly better.Bear runs away" %bear
		
elif door== "2":
        print "you stare into the endless abyss at Cthulhu's retina"
	print "1. blueberries"
	print "2. yellow jacket clothespins"
	print "3. understanding revolvers yelling melodies"
    
	ins= raw_input(">")
	
	if ins == "1" or ins == "2":
	    print "u r survies"
	else:
	    print "good Job..!!"

else:
   print "you stumble around and fall on a knife and die"