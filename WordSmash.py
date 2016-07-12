import random
import os

while True:
	words = os.listdir("./words")
	wnum=random.choice(words)
	
	dirfiles = os.listdir("./words/" + wnum)
	word=""
	for filen in dirfiles:
		if ( (filen[-2:]) == ".d"):
			word = filen[:-2]
			wordguess = "_ " * len(word)
			deffile = open("./words/" + wnum + "/" + filen, "r")
			yrguess=""
			while yrguess != word:
				for defs in deffile.readlines():
					print (defs[:-1])
				print wordguess
				yrguess = raw_input("")
				yrguess = yrguess[:+len(word)]
				if (yrguess == "c"): #clue					
					charpos = random.randint(0,len(word)-1)

					yrguess = " "*(charpos) + word[charpos]

				let=0
				for l in list(yrguess):
					wglist=list(wordguess)
					if (l == word[let]):
						wglist[let*2]=l
					wordguess = "".join(wglist)
					let +=1

