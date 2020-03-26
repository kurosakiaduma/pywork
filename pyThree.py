xDict = {
        "Name" : "The Lion King",
        "Year of release" : 2003,
        "Rating" : "B+"
}

print(xDict)

def myfunc():
 x = xDict["Name"]
 print("The whole day I watched", x)

def myfuncTwo():
 for x in xDict:
     print(x, ":", xDict[x])

myfunc()
myfuncTwo()

