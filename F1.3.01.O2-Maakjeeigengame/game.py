import time
import getpass

def path1(irritation, textspeed):
    print("the sun is shining, the warmth feels great on ur skin")
    time.sleep(2 / textspeed)
    print("u see your car, it's your favorite car. what do you want to do?")
    loop = True
    while loop == True:
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif "back" in input1[0]:
            print("WHY, i, i mean, okay let's go back inside")
            loop = False
            irritation += 3
            time.sleep(2 / textspeed)
            print("u did it just to annoy me didn't u?")
            return 1, irritation
    







def path2(irritation, textspeed):
    e = 1



textspeed = 2
irritation = 0
sad = 0
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
        print("are you really trying to get me mad before the game even started? lol")
        time.sleep(2 / textspeed)
        funnyanswer +=1
        irritation -= 1
    elif (input1[0] == "enter" or input1[0] == "Enter") and funnyanswer == 1:
        print("no...")
        time.sleep(1 / textspeed)
        print("fine, i'll start it")
        loop = False
        time.sleep(2 / textspeed)
    elif input1[0] != "":
        print(f"i said, press enter to start, not 'press {input1[0]} to start'")
        time.sleep(1 / textspeed)
    else:
        loop = False
        time.sleep(1 / textspeed)

print("welcome " +getpass.getuser() + ". you just woke up, it's beautiful outside")
loop = True
while loop == True:
    time.sleep(2 / textspeed)
    print("what do you want to do?")
    time.sleep(1 / textspeed)
    print(">1.go outside< \n >2.stay inside<")
    input1 = input("press Enter to start ").split('.',1)
    if input1[0] == "speed":
        textspeed = float(input1[1])
        print(f"someGoodSpeedChangeFeedback {textspeed}")
    elif input1[0] == "":
        print("What about choosing")
        time.sleep(1 / textspeed)
    else:
        if input1[0] == "go outside" or input1[0] == "1":
            print("yes!")
            loop = False
            time.sleep(1 / textspeed)
            end, irritation = path1(irritation, textspeed)
            if end == 1:
                path2(irritation, textspeed)
        elif input1[0] == "stay inside" or input1[0] == "2":
            loop = False
            print("Why tho?")
            irritation +=1
            time.sleep(2 / textspeed)
            path2(irritation, textspeed)
        else:
            print("what about choosing one of the options")