xList = ["new","list"]

xTuple = ("apple", "banana", "cherry")
yTuple = ("cow", "monkey", "dog")
zTuple = ("yellow")

xSet = {"left", "right", "up", "down"}
ySet = {"motors", "bikes"}
print(xSet)
zSet = xSet.union(ySet)
print(zSet)

def myfuncOne():
 ySet = xSet.pop()
 print(ySet)
 xSet.add("zigzag")
 print(xSet)

def myfuncTwo():
 for x in xTuple:
     print(x)

def myfunc():
 y = list(xTuple)
 y[0]="kiwi"
 print(y)

def myfuncThree():
 newTuple = xTuple + yTuple
 print(newTuple)

def myfuncFour():
 print(xList)
 xxTuple = tuple(xList)
 print(xxTuple)

myfunc()
myfuncOne()
myfuncTwo()
myfuncThree()
myfuncFour()
