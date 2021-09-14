import time
textspeed = 2
irritation = 0
sad = 0
print("welcome to 'Mom! I accidentally gave little brother cocaine!'")
print("want to change text speed? say speed.(the textspeed number) to change it")
loop = True
funnyanswer = 0
while loop == True:
    input1 = input("press Enter to start ").split('.',1)
    if input1[0] == "speed":
        textspeed = float(input1[1])
        print(f"someGoodSpeedChangeFeedback {textspeed}")
    elif (input1[0] == "enter" or input1[0] == "Enter") and funnyanswer == 0:
        print("haha i see, so you are the person you hope people reffer to as funny. but u know what? they don't")
        time.sleep(2 / textspeed)
        funnyanswer += 1
        irritation += 1
    elif (input1[0] == "enter" or input1[0] == "Enter") and funnyanswer >= 55:
        print("get a life, u did say 'enter' 55 times.")
        sad = 100
        time.sleep(2 / textspeed)
    elif (input1[0] == "enter" or input1[0] == "Enter") and funnyanswer > 6:
        print("this... is just sadd")
        funnyanswer += 1
        time.sleep(2 / textspeed)
        sad = 1
    elif (input1[0] == "enter" or input1[0] == "Enter") and funnyanswer > 0:
        print("You know, when u do it again, it doesn't make it more annoying, it just makes me realize how sad of a human being you are")
        funnyanswer += 1
        time.sleep(2 / textspeed)
    elif input1[0] != "":
        print(f"i said, press enter to start, not 'press {input1[0]} to start'")
        time.sleep(1 / textspeed)
    else:
        loop = False
print()
print("ehm, yeah didn't think you would get this far, wait.")
time.sleep(4 / textspeed)
print()
print("AAAAAAAH, why does someone actually want to play this")
time.sleep(5 / textspeed)
print("this just exists because the app store looks less empty")
time.sleep(5 / textspeed)
print()
print("you were not supposed to open this, ehm let me create something")
time.sleep(4 / textspeed)
print()
loop = True
while loop == True:
    input1 = input("press Enter to continue ").split('.',1)
    if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
    elif (input1[0] == "enter" or input1[0] == "Enter"):
        print("Why, just why. it's not funny, like not at all.")
        time.sleep(2 / textspeed)
        print("ah whatever, ur a sad human being")
        loop = False
        irritation += 1
    elif input1[0] != "":
        print(f"i said, press enter to continue, not 'press {input1[0]} to continue'")
        time.sleep(2 / textspeed)
        print(f"ah whatever, {input1[0]} is good enough")
        loop = False
    else:
        print("i love it that some people actually do what u ask them to")
        loop = False
time.sleep(3 / textspeed)
print()
print("okay ehhm, so what are people into these days?")
time.sleep(5 / textspeed)
print("oh yeah, you are a person, what are people into these days? ")
loop = True
while loop == True:
    input1 = input(">>> ").split('.',1)
    if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
    elif input1[0] == "":
        print("That's nothing, u twat")
    else:
        loop = False
print()
print(f"hmmm, {input1[0]} u say?")
time.sleep(2 / textspeed)
print(f"the fact that U, the person that wanted to play this, says {input1[0]} makes me question it")
time.sleep(3 / textspeed)
