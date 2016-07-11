import re
import os 
print os.listdir(".")
file = open("*.def",'r')
defpat= ' -- \(([^\n;]*)'
defpat2= '\)\n'
g = file.readlines()
for line in g:
	m = re.search(defpat, line)
	if m:
		if m.group(1) != "":
			if (m.group(1).endswith(")")):
				print m.group(1)[:-1]
			else:
				print (m.group(1))
