def fibonacci(fullNumber,loopNumber):
    midNumber = 0
    midNumber = fullNumber + loopNumber
    loopNumber = fullNumber
    fullNumber = midNumber
    print(fullNumber)
    return fullNumber,loopNumber
lastNumber = 0
thisNumber = 1
loopTime = int(input("how many times?\n"))
print("\n0\n1")
for x in range(0,loopTime):
    thisNumber,lastNumber = fibonacci(thisNumber,lastNumber)
print(f"\n\n{thisNumber}")