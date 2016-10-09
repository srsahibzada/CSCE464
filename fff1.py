minrange = int(input('enter the filenum: '))
numincr = 0
with open('avgs.txt') as f:
	for line in f:
		
		if ('out'+str(minrange)+'.txt') in line:
			print line
