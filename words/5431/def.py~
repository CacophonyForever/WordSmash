import re
import os 
dirfiles = os.listdir(".")
for filen in dirfiles:
	if ( (filen[-4:]) == ".def"):
		wordname = filen[:-4]
		file = open(filen,'r')
		wordpat = "Overview of (.*?) (.*?)$"
		defpat= ' -- \(([^\n;]*)'
		defpat2= '\)\n'
		g = file.readlines()
		out = []
		for line in g:
			w = re.search(wordpat, line)
			if w:
				wordname = w.group(2)
			m = re.search(defpat, line)
			if m:
				if m.group(1) != "":
					if (m.group(1).endswith(")")):
						out.append(m.group(1)[:-1])
					else:
						out.append((m.group(1)))
		for defin in out:
			print defin
		print (wordname)
