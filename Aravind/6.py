thislist = ["a","b","c","d"]
length = len(thislist)
thislist[0],thislist[length-1] = thislist[length-1],thislist[0]
print thislist