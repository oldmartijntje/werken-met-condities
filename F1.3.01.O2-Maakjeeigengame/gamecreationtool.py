import os.path
import os
input = input(">>>").split('.',1)
if input[0] == "load":
    if os.path.isfile(input[1]+".txt"):
        receipt = open(input[1]+".txt", "a")
    else:
        receipt = open(input[1]+".txt", "x")
