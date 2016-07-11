import re
import os 
dirfiles = os.listdir(".")
for filen in dirfiles:
	if ( (filen[-4:]) == ".def"):
		wordname = filen
		print (wordname)
		file = open(filen,'r')
		defpat= ' -- \(([^\n;]*)'
		defpat2= '\)\n'
		g = file.readlines()
		out = []
		for line in g:
			m = re.search(defpat, line)
			if m:
				if m.group(1) != "":
					if (m.group(1).endswith(")")):
						out.append(m.group(1)[:-1])
					else:
						out.append((m.group(1)))
		for defin in out:
			print defin
