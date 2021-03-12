import sys

itemset=[90,85,94,102,110]



newlist = []
newset=[]



with open(sys.argv[1],'rt') as myfile:


   # for k in itemset:


            for mylines in myfile:

                    if int(mylines.split()[1]) in itemset:
                        newset.append(int(mylines.split()[1]))

print(newset.reverse())











#templist=sorted(newset)


#for y in templist:
 #   index = newset.index(y)
  #  secondlist.append(itemset[index])

#itemset.clear()
#itemset.extend(secondlist)
#print(itemset)

















