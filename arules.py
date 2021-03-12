import sys
import time
import itertools
if __name__ == '__main__':

    startTime = time.time()
# ======================================================================================

    def powerset(s,rsize):
        return list(itertools.combinations(s, rsize))


    def toString(list):

        mystr = ""


        for e in list:
            mystr = mystr + str(e) + ' '


        return mystr.strip()

#==================================================================================

    slist=[]
    plist=[]
    chklist=[]
    dlist=[]

    conf = float(sys.argv[3])

    jfile = sys.argv[1]
    kfile = sys.argv[2]

    mydict={}
    y=0
    myset=[]

    count=0

    with open(sys.argv[1], 'r', encoding='utf-8') as myjfile:

        for mylines in myjfile:

            y = len(mylines.split())
            y = y - 1

            for x in range(y):
                myset.append(int(mylines.split()[x+1]))

            mydict[frozenset(myset)] = int(mylines.split()[0])
            myset.clear()


    myjfile.close()



    with open(sys.argv[2], 'r', encoding='utf-8') as mykfile:

        for myline in mykfile:

            a = len(myline.split())
            a = a - 1
            jsupport = int(myline.split()[0])

            for v in range(a):
                slist.append(int(myline.split()[v + 1]))

            chklist=list(powerset(slist,y))
            for h in chklist:

                if frozenset(h) in mydict:

                    ksupport = mydict.get(frozenset(h))

                    theconf = jsupport / ksupport

                    if theconf >= conf:

                        dlist= set(slist) - set(h)
                        count = count + 1


                        print(f"{theconf:.3f}" + ' ' + toString(h) + ' => ' + toString(dlist))
                else:
                    continue



            slist.clear()
            chklist.clear()


    endTime = time.time()
