# Deepak Singh
# Ex.1a, b, c, d, e

alist = []
alist.append('apple')
blist = []
for i in range(20):
    blist.append(0)
def inputFunc():
    clist = []
    clist = alist + blist
    print(clist)
    lastC = clist.pop()
    print(clist)

inputFunc()
