import os
count=0
sval = 1
dirname = raw_input("Where are your delay files stored? : ")

files = os.listdir(dirname+"/")
os.chdir(dirname+"/")
for f in files:
    with open(f) as each:
        #print f
	val = 0;
        numlines=0
        for line in each:
            numlines += 1
            timeval = line[-12:]
            val += float(timeval)
        print str(val / float(numlines)) + " is the average for " + f + "."
