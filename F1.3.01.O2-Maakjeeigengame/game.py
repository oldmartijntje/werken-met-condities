import time
import getpass
import os
import os.path
if os.path.isfile("traumatix.txt"):
    f = open("traumatix.txt", "a")
else:
    f = open("traumatix.txt", "x")
f.close
def save(irritation, textspeed, cringe):
    
    open('traumatix.txt', 'w').close()
    f = open("traumatix.txt", "a")
    f.write(str(cringe)+";"+str(irritation)+";"+str(textspeed))
def path1(irritation, textspeed, cringe):
    print("the sun is shining, the warmth feels great on ur skin")
    time.sleep(2 / textspeed)
    print("u see your car, it's your favorite car. what do you want to do?")
    loop = True
    while loop == True:
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif input1[0] == "game":
            if input1[1]== "save":
                save(irritation,textspeed,cringe)
                print(f"someGoodSavingFeedback")
            elif input1[1]=="exit":
                save(irritation,textspeed,cringe)
                exit()
        elif "back" in input1[0] or "inside" in input1[0]:
            print("WHY, i, i mean, okay let's go back inside")
            loop = False
            irritation += 3
            time.sleep(2 / textspeed)
            print("u did it just to annoy me didn't u?")
            return 1, irritation, cringe
        elif "car" in input1[0]:
            print("i knew you would want to go inside that car")
            time.sleep(2 / textspeed)
            loop = False
        elif ("dance" or input1[0] or "dab" in input1[0] or "die" in input1[0] or "yeet" in input1[0]) and cringe < 5:
            if "dance" in input1[0]:
                print("U decided to do a fortnite dance for some reason")
                time.sleep(2 / textspeed)
                cringe += 1
                print("100 precent cringe")
            elif "dab" in input1[0] and cringe <= 2:
                print("u decided to dab, i should get this feature removed")
                cringe += 1
                time.sleep(3 / textspeed)
            elif "dab" in input1[0] and cringe == 3:
                print("u decided to dab, i am going to remove this feature")
                cringe += 1
                time.sleep(3 / textspeed)
            elif "dab" in input1[0] and cringe == 4:
                print("u decided to dab, haha it's deleted now")
                cringe += 3
                time.sleep(1 / textspeed)
            elif "dab" in input1[0] and cringe == 5:
                print("u decided to dab, dangit, now it should be deleted")
                cringe += 3
                time.sleep(1 / textspeed)
            elif "die" in input1[0]:
                print("no")
                time.sleep(2 / textspeed)
            elif "yeet" in input1[0]:
                print("no, there is nothing to yeet")
                time.sleep(2 / textspeed)
        else:
            print("i didn't get that, please be clearer, keywords like 'car' and 'inside' will work")
            time.sleep(5 / textspeed)
    







def path2(irritation, textspeed, cringe):
    e = 1

with open('traumatix.txt') as f:
    if ';' in f.read():
        f.close
        f =open("traumatix", "r")
        reading = f.read().split(';',4)
        cringe = int(reading[2])
        irritation = int(reading[0])
        textspeed = float(reading[1])
        played = True
    else:
        cringe = 0
        textspeed = 2
        irritation = 0
        sad = 0
        loop = True
        funnyanswer = 0
        played = False
f.close

if played == False:
    while loop == True:
        input1 = input("press Enter to start ").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif input1[0] == "game":
            if input1[1]== "save":
                save(irritation,textspeed,cringe)
                print(f"someGoodSavingFeedback")
            elif input1[1]=="exit":
                save(irritation,textspeed,cringe)
                exit()
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
save(irritation,textspeed,cringe)
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
    elif input1[0] == "game":
        if input1[1]== "save":
            save(irritation,textspeed,cringe)
            print(f"someGoodSavingFeedback")
        elif input1[1]=="exit":
            save(irritation,textspeed,cringe)
            exit()
    elif input1[0] == "":
        print("What about choosing")
        time.sleep(1 / textspeed)
    else:
        if input1[0] == "go outside" or input1[0] == "1":
            print("yes!")
            loop = False
            time.sleep(1 / textspeed)
            end, irritation, cringe = path1(irritation, textspeed, cringe)
            if end == 1:
                path2(irritation, textspeed, cringe)
        elif input1[0] == "stay inside" or input1[0] == "2":
            loop = False
            print("Why tho?")
            irritation +=1
            time.sleep(2 / textspeed)
            path2(irritation, textspeed, cringe)
        else:
            print("what about choosing one of the options")