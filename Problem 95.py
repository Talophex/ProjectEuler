
# coding: utf-8

# In[58]:


import math

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(math.sqrt(n))+1, step) if n % i == 0)))

def FindAllDivisors(x):
    divList = [1]
    y = 2
    while y <= math.sqrt(x):
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    return sorted(divList)

amdict = dict()

for i in xrange(2,2000):
    newentry = factors(i)
    newentry.discard(i)
    if sum(newentry) > 1 and sum(newentry) != i:
        amdict[i] = sum(newentry)

keepgoing = True
while keepgoing:
    tobewiped = []
    for key in amdict:
        if amdict[key] not in amdict:
            tobewiped.append(key)
    if len(tobewiped) > 0:
        #print tobewiped
        for tobe in set(tobewiped):
            del amdict[tobe]
    else:
        keepgoing = False
    
print amdict

