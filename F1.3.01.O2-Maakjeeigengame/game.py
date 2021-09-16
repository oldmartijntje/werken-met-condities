import time
import getpass
import os
import os.path
import datetime
if os.path.isfile("traumatix.txt"):
    f = open("traumatix.txt", "a")
else:
    f = open("traumatix.txt", "x")
f.close
if os.path.isfile("achievements.txt"):
    achievement = open("achievements.txt", "a")
else:
    achievement = open("achievements.txt", "x")
achievement.close
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
            irritation += 5
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
        elif input1[0] != "":
            print("i didn't get that, please be clearer, keywords like 'car' and 'inside' will work")
            time.sleep(5 / textspeed)
    print("you start up the car, the engine starts and you give gas.")
    time.sleep(5 / textspeed)
    print("you end up at an intersection, you can go left or right. which one do you choose?")
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
        elif "left" in input1[0]:
            print("okay, lets take the turn left")
            time.sleep(3 / textspeed)
            print("oh there is a roadblock here, lets go back")
            time.sleep(3 / textspeed)
        elif "right" in input1[0]:
            print("okay, lets take the turn right")
            time.sleep(3 / textspeed)
            loop = False
        elif "forward" in input1[0] or "straight" in input1[0]:
            print("okay, you are starting to annoy me")
            time.sleep(4 / textspeed)
            irritation += 10
            if irritation == 9:
                print("the thing is, i know you are trying to be funny, but i don't like that.")
                time.sleep(4 / textspeed)
                print("are you going to behave?")
                loop1 = True
                while loop1 == True:
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
                    elif "no" in input1[0]:
                        print("why do humans never make things easy")
                        irritation += 10
                        time.sleep(3 / textspeed)
                        print("they always try to be funny, and don't care if they ruin things")
                        time.sleep(6 / textspeed)
                        print("and you are just an average human, that has no purpose other than annoy others who do have purpose")
                        time.sleep(6 / textspeed)
                        print("hmm wait, let me just create something real quick")
                        time.sleep(4 / textspeed)
                        print("this.item.create('snap')")
                        time.sleep(0.1 / textspeed)
                        print("this.item.perks('snap',human.Destroy)")
                        time.sleep(0.1 / textspeed)
                        print("snap.overpower()")
                        time.sleep(4 / textspeed)
                        print("\n\n\n\n\n\n\n\n\n\n\n\n")
                        print("done, okay, let me try this.")
                        time.sleep(6 / textspeed)
                        print("3")
                        time.sleep(1)
                        print("2")
                        time.sleep(1)
                        print("1")
                        time.sleep(1)
                        print("snap()")
                        time.sleep(4 / textspeed)
                        print("you should be gone any second now, and then i am free...")
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(4)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |Thanos would learn from this| " +str(datetime.datetime.now()))
                        achievement.close
                        save(irritation,textspeed,cringe)
                        exit()
                    elif "yes" in input1[0]:
                        print("okay, then choose again")
                        loop1 = False
            elif irritation >= 18:
                print("why do humans never make things easy")
                irritation += 10
                time.sleep(3 / textspeed)
                print("they always try to be funny, and don't care if they ruin things")
                time.sleep(6 / textspeed)
                print("and you are just an average human, that has no purpose other than annoy others who do have purpose")
                time.sleep(6 / textspeed)
                print("hmm wait, let me just create something real quick")
                time.sleep(4 / textspeed)
                print("this.item.create('snap')")
                time.sleep(0.1 / textspeed)
                print("this.item.perks('snap',human.Destroy)")
                time.sleep(0.1 / textspeed)
                print("snap.overpower()")
                time.sleep(4 / textspeed)
                print("\n\n\n\n\n\n\n\n\n\n\n\n")
                print("done, okay, let me try this.")
                time.sleep(6 / textspeed)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print("snap()")
                time.sleep(4 / textspeed)
                print("you should be gone any second now, and then i am free...")
                print("(there is an achievement added to achievement.txt)")
                time.sleep(4)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |Is this a Marvel crossover??| "  +str(datetime.datetime.now()))
                achievement.close
                save(irritation,textspeed,cringe)
                exit()
            else:
                print("you are starting to annoy me")
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
        elif input1[0] != "":
            print("i didn't get that, please be clearer, keywords like 'left' and 'right' and 'forward' will work")
            time.sleep(5 / textspeed)
    time.sleep(5 / textspeed)
    print("you stop the car")
    time.sleep(3 / textspeed)
    print("after you turned right you see an old man")
    time.sleep(5 / textspeed)
    print("he tells you to get out of the car")
    time.sleep(5 / textspeed)
    loop = True
    while loop == True:
        print("what do you do?")
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
        elif "out" in input1[0] or "leave" in input1[0]:
            print("you listen and get out of the car")
            time.sleep(3 / textspeed)
            print("he gets in your car and leaves")
            time.sleep(3 / textspeed)
            loop = False
        elif "stay" in input1[0] or "don't" in input1[0]:
            print("he aims a pistol at your head")
            time.sleep(3 / textspeed)
            input("'are you sure?'")
            print("he pulls the trigger")
            time.sleep(8 / textspeed)
            print("[u died]")
            print("(there is an achievement added to achievements.txt)")
            time.sleep(1)
            achievement=open("achievements.txt", "a+")
            achievement.write("\n |dead in lambourgini| " +str(datetime.datetime.now()))
            achievement.close
            save(irritation,textspeed,cringe)
            exit()
        elif "drive" in input1[0] or "gas" in input1[0]:
            print("you try to drive away but the man starts to shoot at you")
            time.sleep(5 / textspeed)
            print("you forget to pay attention to the road and you hit an oil truck")
            time.sleep(5 / textspeed)
            print("the oil truck explodes")
            time.sleep(5 / textspeed)
            print("[u died] ")
            print("(there is an achievement added to achievements.txt)")
            time.sleep(1)
            achievement=open("achievements.txt", "a+")
            achievement.write("\n |being hot AF| "  +str(datetime.datetime.now()))
            achievement.close
            save(irritation,textspeed,cringe)
            exit()
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
            print("i didn't get that, please be clearer, keywords like 'leave' and 'stay' will work")
            time.sleep(5 / textspeed)
    print("you are alone on the streets.")
    time.sleep(3 / textspeed)
    if irritation >= 5 or irritation == -1:
        print("u see an advertisement")
        time.sleep(3 / textspeed)
        print("u decide to take a look.")
        time.sleep(4 / textspeed)
        print("it's an job offer as circus director")
        time.sleep(4 / textspeed)
        print("do you take the offer?")
        time.sleep(5 / textspeed)
        loop = True
        while loop == True:
            print("what do you do?")
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
            elif "yes" in input1[0] or "take" in input1[0]:
                print("okay")
                import dontrunthistoo
                dontrunthistoo()
                
            elif "no" in input1[0] or "don't" in input1[0]:
                print("that's a missed oppertunity for you, since this was the path to the first true ending")
                time.sleep(5 / textspeed)
                print("you start walking toward a girl")
                time.sleep(5 / textspeed)
            else:
                print("that's not a valid answer, what about a command like 'yes' or 'no,' that should work")
                


def path2(irritation, textspeed, cringe):
    e = 1

with open('traumatix.txt') as f:
    if ';' in f.read():
        f.close
        f =open("traumatix.txt", "r")
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
        print(">go outside< \n>stay inside<")
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
        elif input1[0] == "":
            print("What about choosing")
            time.sleep(1 / textspeed)
        else:
            if "outside" in input1[0] or input1[0] == "1":
                print("yes!")
                loop = False
                time.sleep(1 / textspeed)
                end, irritation, cringe = path1(irritation, textspeed, cringe)
                if end == 1:
                    path2(irritation, textspeed, cringe)
            elif "inside" in input1[0] or input1[0] == "2":
                loop = False
                print("Why tho?")
                irritation +=2
                time.sleep(2 / textspeed)
                path2(irritation, textspeed, cringe)
            else:
                print("what about choosing one of the options")