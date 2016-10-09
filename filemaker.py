seedvals = [1,2,3,4,5]
pausetimes = [2,5,10,20]
protocols = ['AODV','DSR']
filenum = 0
for val in seedvals:
    #print str(val) + ": val"
    for time in pausetimes:
        #print str(time) + "S"
        for protocol in protocols:
            #print str(protocol) + "protocol"
            with open('seedfile.txt') as seedfile:
                with open('config' + str(filenum) + '.in', 'w') as outfile:
                    #print 'openn sesame'
                    for line in seedfile:
                        if '//' not in line:
                            outfile.write(line)
                        else:
                            # set seed value
                            if "SEED" in line:
                                outfile.write("SEED                "+str(val) +"\n")
                            if "MOBILITY-WP-PAUSE" in line:
                                outfile.write("MOBILITY-WP-PAUSE       "+str(time)+"S"+"\n")
                            if "ROUTING-PROTOCOL" in line:
                                outfile.write("ROUTING-PROTOCOL    "+protocol+"\n")

                filenum += 1
                #print  val, protocol, time
                #print
