
# coding: utf-8

# In[21]:


import urllib2

def Prob102(lst):
    for i in xrange(0,3):
        others = ["0","1","2"]
        others = [int(x) for x in others if str(i) not in str(x)]
        xy = lst[i]
        x1y1 = lst[others[0]]
        x2y2 = lst[others[1]]
        d1 = (xy[0]-x1y1[0])*(x2y2[1]-x1y1[1])-(xy[1]-x1y1[1])*(x2y2[0]-x1y1[0])
        xy = [0,0]
        d2 = (xy[0]-x1y1[0])*(x2y2[1]-x1y1[1])-(xy[1]-x1y1[1])*(x2y2[0]-x1y1[0])
        if d1 > 0:
            if d2 < 0:
                return False
        elif d1 < 0:
            if d2 > 0:
                return False
    return True

ans = 0

rawtext = urllib2.urlopen("https://projecteuler.net/project/resources/p102_triangles.txt")
for line in rawtext:
    coords = []
    for i in xrange(0,5,2):
        newcoord = [int(line.split(",")[i]),int(line.split(",")[i+1])]
        coords.append(newcoord)
    if Prob102(coords) == True:
        ans += 1
print "Answer:"
print ans


# In[17]:




