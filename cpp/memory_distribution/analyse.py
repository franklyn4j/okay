

import sys
from collections import Counter
li = []
for line in sys.stdin:
    data = line.split(":")
    li.append(data[1][1:-1])
for key,value in  Counter(li).items():
    print "%s : %d" % (key,value)
#se = set(li)

#for i in se:
#    print "%d : %d", (i,li.count(i))
