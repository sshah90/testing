from sys import exit

def  gold_room():
	print "This room is full of gold.How much do you take?"

	next=raw_input(">")
	
	how_much=int(next)
	

	if how_much < 50:
		print "Nice, you are not greedy,you win!"
		exit(0)
	elif how_much>=50:
		dead("you greedy bastard!")

	else:
		dead("Man,learn to type a number.")


def bear_room():
	print "there is a bear here"
	print "the bear has bunch of honey"
	print "he fat bear is in front of another door."
	print "how are you going to move the bear?"
	bear_moved= False

	while True:
		next= raw_input(">")

		if next=="take honey":
			dead("the bear look at you then slap your face off.")
		elif next=="taunt bear"and not bear_moved:
			print "the bear has moved from the door.you can go through it now"
			bear_moved=True
		elif next=="taunt bear" and bear_moved:
			dead("the bear gets pissed off and chew your leg off.")
		elif next=="open door" and	bear_moved:
			gold_room()
		else:
			print "i got no idea whay that means."
			exit(0)

def cthulhu_room():
	print "Here you see the great evil cthulhu"
	print "he,it,whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next =raw_input(">")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	print why,"Good Job...!"
	exit(0)


def start():
	print "you are in dark room."
	print "there is a door to your right and left."
	print "which one do you take"

	next = raw_input(">")

	if next =="left":
		bear_room()
	elif next=="right":
		cthulhu_room()
	else:
		dead("you stumble around the room until you starve.")

start()

	