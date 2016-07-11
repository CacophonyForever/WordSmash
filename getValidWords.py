import subprocess
import os
from subprocess import Popen, PIPE
print (subprocess.__file__)
f = open ('wordfreq','r').read().split('\n')
n=1
for line in f:
	text = Popen(["wordnet" , line , "-over"], stdout=PIPE)
	defn = text.stdout.read()
	if (defn != ""):
		print (line + str(n))
		os.mkdir("words/" + str(n))
		w = open("words/" + str(n) + "/" + line + ".def", 'w')
		w.write((defn))
		w.close()
		n = n + 1

