from sys import argv

script,user_name =argv
prompt= '>'

print "hi %s, I'm the %s script" %(user_name,script)
print "I'd like to ask you few questions"
print "Do you like me %s ?" %user_name
likes = raw_input(prompt)

print "where r u leaving?"
lives = raw_input(prompt)

print "what ur r computer name"
name= raw_input(prompt)

print """
so you said %s about liking me.
you live in %s,not sure where it is.
and you have %s computer.nice.
""" %(likes,lives,name)