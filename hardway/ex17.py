from sys import argv
from os.path import exists

script,from_file,to_file =argv

print "copying From %s to %s" % (from_file,to_file)

indata= open (from_file).read()

print "the input file is %d byte long " %len (indata)

print "does the output file exist? %r" %exists (to_file)

print "ready,to hit enter to continue,CTRL+C to abort"
raw_input()

out_file=open(to_file,'w').write(indata)

print "alright,all done"