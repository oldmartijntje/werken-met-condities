def helloWorld(num:int=1):
    for x in range(1, num+1):
        print(f"{x}.hello World!")
helloWorld(int(input("how many times?")))