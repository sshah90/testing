print "Let's practice everything"

print "you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs"

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern\n the need of love
nor comprehend passion from intution
and require an explanation
\n\t\t where there is none.
"""
print "-"*10,
print poem,
print "-"*10

five = 10-2+3-6
print "this should be five: %s" %five

def secret_formula(s):
    jelly_beans=s*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates
	
start_point=10000
beans,jars,crates=secret_formula(start_point)

print "with a starting point %d" %start_point
print "we'd have %d beans, %d jars and %d crates" %(beans,jars,crates)

start_point/=10

print "we can do this way too"
print "now we have %d jars,%d beans and %d crates" %secret_formula (start_point)