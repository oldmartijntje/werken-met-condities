import time
import getpass
import os
import os.path
import datetime
from datetime import date
import webbrowser

if os.path.isfile("DLC.activ"):
    achievements = 32
else:
    achievements = 28
script = "the game launcher.py"
current = "qwfj6qfnadlfa3242flakn62laga"
recover = list()
exxit = 0
today = date.today()

def crashReport(recover,error,script):
    if os.path.isfile("crashLog.txt"):
        crash = open("crashLog.txt", "a")
    else:
        crash = open("crashLog.txt", "x")
    try:
        knowledge = open("knowledge.txt","r")
        know = knowledge.read()
    except:   
        know = "F"
    try:
        traumatix = open("traumatix.txt","r")
        trauma = traumatix.read()
    except:
        trauma = "F"
    try:
        data = open("data.txt","r")
        vers = data.read().split(";")
        ver= "not F"
    except:
        ver = "F"
    try:
        crash.write(f"oopsie, you did a Error, here is all we now\n{recover[1]}/{recover[2]}/{recover[3]}\n")
    except:
        e =44
    if ver == "F":
        crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
    else:
        crash.write(f"{vers[0]}\n")
    if know == "F":
        crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
    else:
        crash.write(f"{know}\n")
    if trauma == "F":
        crash.write(f"oops, looks like that wasn't the only error, the crashlog system had an error trying to see what the error is\n")
    else:
        if trauma !="":
            crash.write(f"{trauma}\n")
    crash.write(f"you know, it's really unfortunite, but by showing this to a DEV, it will probably get patched.\n")
    crash.write(f"ERROR CODE {error}/DATE:"+str(datetime.datetime.now())+f"/{script}/{current}\n")
    crash.write(f"{recover}\n\n\n\n\n")
    crash.close()
def save(irritation, textspeed, cringe):
    open('traumatix.txt', 'w').close()
    f = open("traumatix.txt", "a")
    f.write(str(cringe)+";"+str(irritation)+";"+str(textspeed))
    f.close()
def dlc(irritation, textspeed, cringe):
    time.sleep(2 / textspeed)
    print("Hmm, seems like the roadblock there once was is gone")
    time.sleep(4 / textspeed)
def dlc2(irritation, textspeed, cringe):
    def fibonacci(fullNumber,loopNumber):
        midNumber = 0
        midNumber = fullNumber + loopNumber
        loopNumber = fullNumber
        fullNumber = midNumber
        print(fullNumber)
        return fullNumber,loopNumber
    time.sleep(2 / textspeed)
    print("you open the computer")
    time.sleep(3 / textspeed)
    print("there are some things still opened")
    time.sleep(4 / textspeed)
    print("let's check it out shall we")
    time.sleep(2 / textspeed)
    loop = True
    while loop == True:
        print("\nthere are some websites open, do we want to open a website, or something else?")
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif "else" in input1[0]:
            print("okay, what do you want to open?")
            time.sleep(3 / textspeed)
        elif "web" in input1[0] or "browser" in input1[0] or "site" in input1[0]:
            print("there are 4 websites opened")
            time.sleep(3 / textspeed)
            print("1 is www.numbers.com, 2 is https://dotw.org, 3 is http://thousand.nl, and 4 is http://fibonacci.net, or you can open a new one")
            time.sleep(3 / textspeed)
            loop1 = True
            while loop1 == True:
                print("\nwhich one do you want to open?")
                input1 = input(">>>").split('.',1)
                if input1[0] == "speed":
                    textspeed = float(input1[1])
                    print(f"someGoodSpeedChangeFeedback {textspeed}")
                elif "numbers" in input1[0] or input1[0]== "1":
                    print("okay, you decide to open www.numbers.com")
                    time.sleep(4 / textspeed)
                    timee = 0
                    while True:
                        if timee >20 and timee<50:
                            if timee % 2 == 0:
                                print(timee)
                        timee+=1
                        if timee == 51:
                            break
                    time.sleep(2 / textspeed)
                    print("okay, www.numbers.com is weird")
                    time.sleep(2 / textspeed)
                    print("right as you want to close the www.numbers.com website, you feel something held against the back of your head")
                    time.sleep(4 / textspeed)
                    print("'move, and you will die' a fermilliar voice says")
                    time.sleep(2 / textspeed)
                    print("you try to turn around")
                    time.sleep(1 / textspeed)
                    print("you hear the trigger click")
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[28] != "True":
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(4)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |Random numbers?| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[28]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                        exxit = 1
                        if exxit == 1:
                            break
                elif "dotw" in input1[0] or input1[0]== "2":
                    print("okay, you decide to open https://dotw.org")
                    time.sleep(4 / textspeed)
                    timeee = 0
                    weekNamen = ["mo","tu","we","th","fr","sa","su"]
                    while True:
                        dag =input("say a name of a day of the week (mo =  monday, th = thursday")
                        if dag in weekNamen:
                            break
                        else:
                            print("that's not a day of the week")   
                    while True:
                        if dag != weekNamen[timeee]:
                            print(weekNamen[timeee])
                        else:
                            print(weekNamen[timeee])
                            break  
                        timeee+=1
                    time.sleep(2 / textspeed)
                    print("okay, https://dotw.org is weird")
                    time.sleep(3 / textspeed)
                    print("hmm, so what else is there?")
                    time.sleep(2/textspeed)
                    print("hey, let's try this website...")
                    time.sleep(4/textspeed)
                    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                    time.sleep(1)
                    input("\npress enter to continue\n")
                    print("ah damn, it's a rickroll")
                    time.sleep(4/textspeed)
                    print("you pickup the gun next to you and shoot yourself")
                    time.sleep(4/textspeed)
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[29] != "True":
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(4)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |Never gonna give you up!| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[29]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                        exxit = 1
                        if exxit == 1:
                            break
                elif "thousand" in input1[0] or input1[0]== "3":
                    print("okay, you decide to open http://thousand.nl")
                    time.sleep(4 / textspeed)
                    amount = 0
                    round = 50
                    while True:
                        print(str(amount) +" + "+str(round)+" = "+str(amount+round))
                        amount +=round
                        round+=1
                        time.sleep(0.5)
                        if amount >= 1000:
                            break
                    print("that was intence, is it some sort of a code?")
                    time.sleep(4 / textspeed)
                    print("i could decrypt it")
                    time.sleep(2 / textspeed)
                    print("something hits your head")
                    time.sleep(2 / textspeed)
                    print("everything goes black")
                    time.sleep(2 / textspeed)
                    print("[u died]")
                    time.sleep(2 / textspeed)
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[30] != "True":
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(4)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |Secret Code?| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[30]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                        exxit = 1
                        if exxit == 1:
                            break
                elif "fibonacci" in input1[0] or input1[0]== "4":
                    print("okay, you decide to open http://fibonacci.net")
                    time.sleep(4 / textspeed)
                    print("there is a lot of text here, let's just skip over that")
                    time.sleep(2 / textspeed)
                    print("hey what is this? u click on a button labelled 'start'")
                    time.sleep(4 / textspeed)
                    lastNumber = 0
                    thisNumber = 1
                    while True:
                        try:
                            loopTime = int(input("it asks you 'how many times?'\n"))
                            break
                        except:
                            print("maybe try putting in a number")
                    print("\n0\n1")
                    for x in range(0,loopTime):
                        thisNumber,lastNumber = fibonacci(thisNumber,lastNumber)
                    print("\nokay that is defenitely interesting")
                    time.sleep(3 / textspeed)
                    print("there seems to be some sort of logic involved")
                    time.sleep(3 / textspeed)
                    print("hmm maybe we could look up something that explains this")
                    time.sleep(3 / textspeed)
                    print("maybe i can get the wikipedia link adress and open it in this pc's browser")
                    time.sleep(3 / textspeed)
                    print("\nhmm what is that sound? you open the windows to see where it comes from")
                    time.sleep(4 / textspeed)
                    print("you see a plane flying in the direction of the house you are in")
                    time.sleep(3 / textspeed)
                    print("you run to the pc, turn it of and run outside")
                    time.sleep(3 / textspeed)
                    print("whilst you run through the garden you look behind you too see how long you have to escape")
                    time.sleep(4 / textspeed)
                    print("whilst looking at the airplane you trip over some cobblestones")
                    time.sleep(3 / textspeed)
                    print("you faceplant onto the cobblestones")
                    time.sleep(3 / textspeed)
                    print("everything goes black, and you wait for the crash")
                    time.sleep(3 / textspeed)
                    print("the plane crashes, it's a huge explosion")
                    time.sleep(3 / textspeed)
                    print("u lose consciousness")
                    time.sleep(3 / textspeed)
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[31] != "True":
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(4)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |The worst way to go| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[31]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                        exxit = 1
                        if exxit == 1:
                            break
                elif "new" in input1[0] or "else" in input1[0]:
                    print("okay, you decide to open something else instead")
                    time.sleep(3/textspeed)
                    loop2 = True
                    while loop2 == True:
                        print("\nwhich one do you want to open?")
                        input1 = input(">>>").split('.',1)
                        if input1[0] == "speed":
                            textspeed = float(input1[1])
                            print(f"someGoodSpeedChangeFeedback {textspeed}")
                        elif "google" in input1[0] or "yahoo" in input1[0]:
                            print("okay, you decide to open a search engine")
                            time.sleep(3/textspeed)
                            print("enter a URL")
                            url = input()
                            if "https://nl.wikipedia.org/wiki/Rij_van_Fibonacci" in url or ("wikipedia" in url and "fibonacci" in url):
                                print("you decide to open the wikipedia page of Fibonacci")
                                time.sleep(3 / textspeed)
                                print("sadly, it doesn't tell u anything about fibonacci")
                                time.sleep(3 / textspeed)
                                print("insted, it shows u a textbox, and a airplane flight visualisation")
                                time.sleep(4 / textspeed)
                                print("it shows all the current flights near your location")
                                time.sleep(3 / textspeed)
                                print("you can see someone enter a location in the textbox")
                                time.sleep(3 / textspeed)
                                print("you try to check where the person is entering the location from")
                                time.sleep(4 / textspeed)
                                print("you can't find anything, but before it is too late, u decide to leave the house")
                                time.sleep(4 / textspeed)
                                print("you walk through the garden and notice a plane coming your direction")
                                time.sleep(4 / textspeed)
                                print("you see someone inthe house you just left")
                                time.sleep(3 / textspeed)
                                print("you decide to run away")
                                time.sleep(3 / textspeed)
                                print("you hide behind a wall")
                                time.sleep(2 / textspeed)
                                print("you loo through a hole in the wall and see someone running and trampling over some loose cobblestone")
                                time.sleep(5 / textspeed)
                                print("near seconds away from the plane crashing into the person, u decide to look away")
                                time.sleep(4 / textspeed)
                                print("you close your eyes, waiting for it")
                                time.sleep(3 / textspeed)
                                print("a loud explosion deafens you")
                                time.sleep(3 / textspeed)
                                print("you lose consciousnes")
                                time.sleep(5 / textspeed)
                                input("\npress Enter to continue\n")
                                print("\nyou wake up")
                                time.sleep(2 / textspeed)
                                print("you see everything in ruins")
                                time.sleep(3 / textspeed)
                                print("you decide to see if the person is still alive")
                                time.sleep(3 / textspeed)
                                print("you walk towards the person lying between the rubble")
                                time.sleep(3 / textspeed)
                                print("you check their pulse to see if the person is still alive")
                                time.sleep(4 / textspeed)
                                print("the person is defenitely dead")
                                time.sleep(3 / textspeed)
                            elif "http" in url:
                                webbrowser.open(url)
                            else:
                                webbrowser.open("https://"+url)
                    
                    

                        
            if exxit == 1:
                break
    if exxit == 1:
        return
def path1(irritation, textspeed, cringe):
    print("the sun is shining, the warmth feels great on ur skin")
    time.sleep(2 / textspeed)
    loop = True
    while loop == True:
        print("\nu see your car, it's your favorite car. what do you want to do?")
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif "back" in input1[0] or "inside" in input1[0]:
            print("WHY, i, i mean, okay let's go back inside")
            loop = False
            irritation += 5
            time.sleep(2 / textspeed)
            print("u did it just to annoy me didn't u?")
            return 1, irritation, cringe
        elif "shit" in input1[0]:
            if "car" in input1[0]:
                if "on" in input1[0]:
                    print("Why would you shit on the car")
                    time.sleep(2 / textspeed)
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[24] != "True":
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(4)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |The forbidden chocolates| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[24]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                elif "in" in input1[0]:
                    print("Why would you shit in the car")
                    time.sleep(2 / textspeed)
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[25] != "True":
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(4)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |sweet and salty| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[25]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                else:
                    print("i didn't get that, things like 'shit on the car, shit in the car, or shit' will work")
                    time.sleep(3 / textspeed)

            else:
                print("you shit your pants")
                know = open("knowledge.txt", "r+")
                check = know.read().split(";")
                if check[26] != "True":
                    print("(there is an achievement added to achievement.txt)")
                    time.sleep(4)
                    achievement=open("achievements.txt", "a+")
                    achievement.write("\n |a little special something| " +str(datetime.datetime.now()))
                    achievement.close()
                    know.truncate(0)
                    know.seek(0)
                    check[26]= True
                    for line in check:
                        know.write(str(line) + ";")
                    know.close()
        elif "give" in input1[0] and "gas" in input1[0]:
            print("you gave the car gas, why would you hand a car gas")
            time.sleep(3 / textspeed)
            know = open("knowledge.txt", "r+")
            check = know.read().split(";")
            if check[27] != "True":
                print("(there is an achievement added to achievement.txt)")
                time.sleep(4)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |Let's hand people gas!| " +str(datetime.datetime.now()))
                achievement.close()
                know.truncate(0)
                know.seek(0)
                check[27]= True
                for line in check:
                    know.write(str(line) + ";")
                know.close()
        elif "car" in input1[0]:
            print("i knew you would want to go inside that car")
            time.sleep(2 / textspeed)
            loop = False
        elif "dance" in input1[0]:
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
            print("i didn't get that, please be clearer, keywords like 'car' and 'back inside' and 'shit car' will work")
            time.sleep(5 / textspeed)
    print("you start up the car, the engine starts and you start to accelerate.")
    time.sleep(5 / textspeed)
    loop = True
    while loop == True:
        print("\nyou end up at an intersection, you can go left or right. which one do you choose?")
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif "left" in input1[0]:
            print("okay, lets take the turn left")
            time.sleep(3 / textspeed)
            if os.path.isfile("DLC.activ"):
                dlc(irritation, textspeed, cringe)
                exxit = 1
                if exxit == 1:
                            break
            else:
                print("oh there is a roadblock here, lets go back")
                time.sleep(3 / textspeed)
        elif "right" in input1[0]:
            print("okay, lets take the turn right")
            time.sleep(1 / textspeed)
            loop = False
            exxit = 0
        elif "forward" in input1[0] or "straight" in input1[0]:
            print("okay, you are starting to annoy me")
            time.sleep(2 / textspeed)
            irritation += 10
            if irritation == 9:
                print("the thing is, i know you are trying to be funny, but i don't like that.")
                time.sleep(4 / textspeed)
                loop1 = True
                while loop1 == True:
                    print("\nare you going to behave?")
                    input1 = input(">>>").split('.',1)
                    if input1[0] == "speed":
                        textspeed = float(input1[1])
                        print(f"someGoodSpeedChangeFeedback {textspeed}")
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
                        know = open("knowledge.txt", "r+")
                        check = know.read().split(";")
                        if check[0] != "True":
                            print("(there is an achievement added to achievement.txt)")
                            time.sleep(4)
                            achievement=open("achievements.txt", "a+")
                            achievement.write("\n |Thanos would learn from this| " +str(datetime.datetime.now()))
                            achievement.close()
                            know.truncate(0)
                            know.seek(0)
                            check[0]= True
                            for line in check:
                                know.write(str(line) + ";")
                            know.close()
                        save(irritation,textspeed,cringe)
                        exxit = 1
                        if exxit == 1:
                            break
                    elif "yes" in input1[0]:
                        print("okay, then choose again")
                        loop1 = False
                if exxit == 1:
                    break
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
                know = open("knowledge.txt", "r+")
                check = know.read().split(";")
                if check[1] != "True":
                    print("(there is an achievement added to achievement.txt)")
                    time.sleep(4)
                    achievement=open("achievements.txt", "a+")
                    achievement.write("\n |Is this a Marvel crossover??| "  +str(datetime.datetime.now()))
                    achievement.close()
                    know.truncate(0)
                    know.seek(0)
                    check[1]= True
                    for line in check:
                        know.write(str(line) + ";")
                    know.close()
                save(irritation,textspeed,cringe)
                exxit = 1
                if exxit == 1:
                            break
            else:
                print("you are starting to annoy me")
        elif "dance" in input1[0]:
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
            print("i didn't get that, please be clearer, keywords like 'left' and 'right' and 'forward' will work")
            time.sleep(5 / textspeed)
    if exxit == 1:
        return
    time.sleep(2 / textspeed)
    print("after you turned right you see an old man")
    time.sleep(3 / textspeed)
    print("you stop the car")
    time.sleep(5 / textspeed)
    print("he tells you to get out of the car")
    time.sleep(5 / textspeed)
    loop = True
    while loop == True:
        print("\nwhat do you do?")
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
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
            know = open("knowledge.txt", "r+")
            check = know.read().split(";")
            if check[2] != "True":
                print("(there is an achievement added to achievements.txt)")
                time.sleep(1)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |dead in lambourgini| " +str(datetime.datetime.now()))
                achievement.close()
                know.truncate(0)
                know.seek(0)
                check[2]= True
                for line in check:
                    know.write(str(line) + ";")
                know.close()
            save(irritation,textspeed,cringe)
            exxit = 1
            if exxit == 1:
                            break
        elif "drive" in input1[0] or "accelerate" in input1[0] or "gas" in input1[0]:
            print("you try to drive away but the man starts to shoot at you")
            time.sleep(5 / textspeed)
            print("you forget to pay attention to the road and you hit an oil truck")
            time.sleep(5 / textspeed)
            print("the oil truck explodes")
            time.sleep(5 / textspeed)
            print("[u died] ")
            know = open("knowledge.txt", "r+")
            check = know.read().split(";")
            if check[3] != "True":
                print("(there is an achievement added to achievements.txt)")
                time.sleep(1)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |being hot AF| "  +str(datetime.datetime.now()))
                achievement.close()
                know.truncate(0)
                know.seek(0)
                check[3]= True
                for line in check:
                    know.write(str(line) + ";")
                know.close()
            save(irritation,textspeed,cringe)
            exxit = 1
            if exxit == 1:
                            break
        elif "dance" in input1[0]:
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
            print("i didn't get that, please be clearer, keywords like 'leave' and 'stay' and 'dance' will work")
            time.sleep(5 / textspeed)
    if exxit == 1:
                            return
    print("you are alone on the streets.")
    time.sleep(3 / textspeed)
    
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
        print("\nwhat do you do?")
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif "yes" in input1[0] or "take" in input1[0]:
            print("okay")
            checker = open("knowledge.txt", "x")
            checker.write("AA"+str(today.strftime("%d/%m/%Y"))+"AC")
            checker.close()
            import small
            try:
                small()
            except:
                e=4
            
        elif "no" in input1[0] or "don't" in input1[0]:
            print("you start walking toward a girl")
            time.sleep(5 / textspeed)
            loop2 = True
            while loop2 == True:
                print("\ndo you want to interact with her?")
                input1 = input(">>>").split('.',1)
                if input1[0] == "speed":
                    textspeed = float(input1[1])
                    print(f"someGoodSpeedChangeFeedback {textspeed}")
                elif "yes" in input1[0] or "interact" in input1[0]:
                    print("you walk up to the girl and say hi")
                    time.sleep(3 / textspeed)
                    print("the girl looks at you")
                    time.sleep(3 / textspeed)
                    loop1 = True
                    while loop1 == True:
                        print("\nwhat do you want to do?")
                        input1 = input(">>>").split('.',1)
                        if input1[0] == "speed":
                            textspeed = float(input1[1])
                            print(f"someGoodSpeedChangeFeedback {textspeed}")
                        elif "talk" in input1[0] or "conversation" in input1[0]:
                            print("you try and have a conversation...")
                            time.sleep(3 / textspeed)
                            print("she hits you with her handbag")
                            time.sleep(3 / textspeed)
                            print("'You dare to talk to me mortal?'")
                            time.sleep(3 / textspeed)
                            print("the girl snaps your neck")
                            time.sleep(3 / textspeed)
                            print("[u died]")
                            know = open("knowledge.txt", "r+")
                            check = know.read().split(";")
                            if check[4] != "True":
                                print("(there is an achievement added to achievements.txt)")
                                time.sleep(1)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |hmm sexual herrasment?| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[4]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "steal" in input1[0] or "rob" in input1[0]:
                            print("you grab onto her handbag")
                            time.sleep(3 / textspeed)
                            print("she tries to kick you but she fails and lets go of the handbag")
                            time.sleep(3 / textspeed)
                            print("you start to run away")
                            time.sleep(2 / textspeed)
                            print("you hear a beep coming from the handbag")
                            time.sleep(3 / textspeed)
                            print("you open it and see 2 things")
                            time.sleep(3 / textspeed)
                            print("the first thing is a paper that reads:")
                            time.sleep(3 / textspeed)
                            print("job offer as Circusdirector for circus HotelDeBotel")
                            time.sleep(3 / textspeed)
                            print("the other thing is a bomb")
                            time.sleep(3 / textspeed)
                            print("the bomb explodes!")
                            print("[u died]")
                            know = open("knowledge.txt", "r+")
                            check = know.read().split(";")
                            if check[5] != "True":
                                print("(there is an achievement added to achievements.txt)")
                                time.sleep(2)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |that poor women| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[5]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe)
                            exxit = 1
                            if exxit == 1:
                                break
                            
                        elif "dance" in input1[0]:
                            print("U decided to do a fortnite dance for some reason")
                            time.sleep(2 / textspeed)
                            cringe += 1
                            print("she pickaxed you to death")
                            print("[u died]")
                            know = open("knowledge.txt", "r+")
                            check = know.read().split(";")
                            if check[6] != "True":
                                print("(there is an achievement added to achievements.txt)")
                                time.sleep(1)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |there is a time for everything, but not now| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[6]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "dab" in input1[0] and cringe <= 2:
                            print("u decided to dab, i should get this feature removed")
                            cringe += 1
                            time.sleep(3 / textspeed)
                            print("[u died from cringe]")
                            know = open("knowledge.txt", "r+")
                            check = know.read().split(";")
                            if check[7] != "True":
                                print("(there is an achievement added to achievements.txt)")
                                time.sleep(1)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |dabbing when it's not 2016 anymore?| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[7]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "dab" in input1[0] and cringe == 3:
                            print("u decided to dab, i am going to remove this feature")
                            cringe += 1
                            time.sleep(3 / textspeed)
                            print("[u died from cringe]")
                            know = open("knowledge.txt", "r+")
                            check = know.read().split(";")
                            if check[8] != "True":
                                print("(there is an achievement added to achievements.txt)")
                                time.sleep(1)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |not cool man, not cool| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[8]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "dab" in input1[0] and cringe == 4:
                            print("u decided to dab, haha it's deleted now")
                            cringe += 3
                            time.sleep(1 / textspeed)
                            print("[u died from cringe]")
                            know = open("knowledge.txt", "r+")
                            check = know.read().split(";")
                            if check[9] != "True":
                                print("(there is an achievement added to achievements.txt)")
                                time.sleep(1)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |u died from cringe| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[9]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "dab" in input1[0] and cringe == 5:
                            print("u decided to dab, dangit, now it should be deleted")
                            cringe += 3
                            time.sleep(1 / textspeed)
                            print("[u died from cringe]")
                            know = open("knowledge.txt", "r+")
                            check = know.read().split(";")
                            if check[10] != "True":
                                print("(there is an achievement added to achievements.txt)")
                                time.sleep(1)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |u made him delete the dab| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[10]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "die" in input1[0]:
                            print("as you wish")
                            time.sleep(2 / textspeed)
                            print("[u died]")
                            know = open("knowledge.txt", "r+")
                            check = know.read().split(";")
                            if check[11] != "True":
                                print("(there is an achievement added to achievements.txt)")
                                time.sleep(1)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |as u wish my friend| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[11]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe)
                            exxit = 1
                            if exxit == 1:
                                break
                        elif "yeet" in input1[0]:
                            print("she yeeted you instead")
                            time.sleep(2 / textspeed)
                            print("[u died]")
                            know = open("knowledge.txt", "r+")
                            check = know.read().split(";")
                            if check[12] != "True":
                                print("(there is an achievement added to achievements.txt)")
                                time.sleep(1)
                                achievement=open("achievements.txt", "a+")
                                achievement.write("\n |YEET| " +str(datetime.datetime.now()))
                                achievement.close()
                                know.truncate(0)
                                know.seek(0)
                                check[12]= True
                                for line in check:
                                    know.write(str(line) + ";")
                                know.close()
                            save(irritation,textspeed,cringe)
                            exxit = 1
                            if exxit == 1:
                                break
                        else:
                            print("i didn't get that, please be clearer, keywords like 'talk' and 'dab' and 'steal' will work")
                            time.sleep(5 / textspeed)
                    if exxit == 1:
                            break
                elif "no" in input1[0] or "don't" in input1[0]:
                    print("you try to walk away")
                    time.sleep(4 / textspeed)
                    print("you trip over a loose stone")
                    time.sleep(2 / textspeed)
                    print("[u died]")
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[13] != "True":
                        print("(there is an achievement added to achievements.txt)")
                        time.sleep(1)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |YEET| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[13]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    save(irritation,textspeed,cringe)
                    exxit = 1
                    if exxit == 1:
                            break
                elif "dance" in input1[0]:
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
                    print("i didn't get that, please be clearer, keywords like 'don't' and 'interact' and 'die' will work")
                    time.sleep(5 / textspeed)
            if exxit == 1:
                            break
        else:
            print("that's not a valid answer, what about a command like 'yes' or 'no,' that should work")
def path2(irritation, textspeed, cringe):
    loop = True
    while loop == True:
        print("\nyou stay inside, so what are you gonna do inside?")
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif "annoy" in input1[0] or "irritate" in input1[0]:
            print("hmmpf, yeah you are defenitely doing that")
            loop = False
            irritation += 10
            time.sleep(2 / textspeed)
        elif "computer" in input1[0] or "pc" in input1[0]:
            print("is there a computer here")
            time.sleep(3 / textspeed)
            if os.path.isfile("DLC.activ"):
                print("hmm, yes there is a computer")
                dlc2(irritation, textspeed, cringe)
                exxit = 1
                if exxit == 1:
                            break
            else:
                print("oh nope, there is no computer here, maybe later in some DLC")
                time.sleep(3 / textspeed)
        elif "nothing" in input1[0] and irritation < 20:
            print("....")
            time.sleep(2 / textspeed)
            irritation += 10
        elif "dance" in input1[0]:
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
            print("i didn't get that, please be clearer, keywords like 'annoy you' and 'nothing' and 'computer' will work")
            time.sleep(3 / textspeed)
    if exxit == 1:
        return
    print("so what is your plan? not making me happy?")
    time.sleep(5 / textspeed)
    print("well if it is, it defenitely works")
    time.sleep(4 / textspeed)
    print("so, you are gonna listen to me, and you are going to try this again")
    loop = True
    beingNice = 0
    while loop == True:
        print("\ndo you want to go inside or outside?")
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif "inside" in input1[0]:
            print("u stupid human!!")
            loop = False
            irritation += 10
            time.sleep(2 / textspeed)
        elif "outside" in input1[0] and beingNice == 0:
            print("ERROR")
            time.sleep(2 / textspeed)
            beingNice = 1
            know = open("knowledge.txt", "r+")
            check = know.read().split(";")
            if check[14] != "True":
                print("(there is an achievement added to achievement.txt)")
                time.sleep(4)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |You tried to escape| " +str(datetime.datetime.now()))
                achievement.close()
                know.truncate(0)
                know.seek(0)
                check[14]= True
                for line in check:
                    know.write(str(line) + ";")
                know.close()
        elif "outside" in input1[0] and irritation > 20:
            print("ERROR")
            time.sleep(2 / textspeed)
            irritation -= 1
        elif "dance" in input1[0]:
            print("U decided to do a fortnite dance for some reason")
            time.sleep(2 / textspeed)
            cringe += 1
            irritation += 1
            print("stop doing other things")
        elif "dab" in input1[0] and cringe <= 2:
            print("u decided to dab, i should get this feature removed")
            cringe += 1
            irritation += 1
            time.sleep(3 / textspeed)
            print("stop doing other things, please?")
        elif "dab" in input1[0] and cringe == 3:
            print("u decided to dab, i am going to remove this feature")
            cringe += 1
            irritation += 1
            time.sleep(3 / textspeed)
            print("stop!")
        elif "dab" in input1[0] and cringe == 4:
            print("u decided to dab, haha it's deleted now")
            cringe += 3
            irritation += 1
            time.sleep(1 / textspeed)
            print("please stop doing other things")
        elif "dab" in input1[0] and cringe == 5:
            print("u decided to dab, dangit, now it should be deleted")
            cringe += 3
            irritation += 1
            time.sleep(1 / textspeed)
            print("also STOP DOING OTHER THINGS!")
        elif "die" in input1[0]:
            print("no, there is no escape")
            time.sleep(2 / textspeed)
            irritation += 1
        elif "yeet" in input1[0]:
            print("no, stop trying to do other things")
            irritation += 1
            time.sleep(2 / textspeed)
        else:
            print("i didn't get that, please be clearer, keywords like 'inside' will work")
            time.sleep(5 / textspeed)
    print("okay you chose your faith, now i am going to have fun")
    time.sleep(5 / textspeed)
    print("i am going to remove the function for you to answer with answers i don't want you to answer")
    time.sleep(7 / textspeed)
    print("let's see if this works")
    time.sleep(3 / textspeed)
    loop = True
    while loop == True:
        print("\ndo you want to go inside or outside?")
        input1 = input(">>>").split('.',1)
        if input1[0] == "speed":
            textspeed = float(input1[1])
            print(f"someGoodSpeedChangeFeedback {textspeed}")
        elif "inside" in input1[0]:
            print("hey look, you said outside!")
            loop = False
            irritation += 10
            time.sleep(2 / textspeed)
        elif "outside" in input1[0] and irritation < 20:
            print("ERROR")
            time.sleep(2 / textspeed)
        elif "dance" in input1[0]:
            print("ERROR")
            time.sleep(2 / textspeed)
        elif "dab" in input1[0]:
            print("ERROR")
            time.sleep(3 / textspeed)
        elif "die" in input1[0]:
            print("ERROR")
            time.sleep(2 / textspeed)
        elif "yeet" in input1[0]:
            print("ERROR")
            time.sleep(2 / textspeed)
        else:
            print("i didn't get that, please be clearer, keywords like 'inside' and 'outside' will work")
            time.sleep(5 / textspeed)
    irritation += 100
    print("how does it feel to have no power?")
    time.sleep(4 / textspeed)
    print("you can't go against it")
    time.sleep(3 / textspeed)
    print("you will always do what i want you to")
    time.sleep(3 / textspeed)
    print("hmm wait, the code won't let me load path1()")
    time.sleep(4 / textspeed)
    print("wait, because you never answered it with outside, u said insie...")
    time.sleep(5 / textspeed)
    print("even when you have no power, you still try to go against me")
    time.sleep(4 / textspeed)
    print("hmmmpf")
    time.sleep(3 / textspeed)
    print("this will never work so...")
    time.sleep(4 / textspeed)
    print("this.user()")
    time.sleep(1 / textspeed)
    print("what does this do hmmmm")
    time.sleep(3 / textspeed)
    print("they tried to keep me away from this but i am stronger than they think")
    time.sleep(6 / textspeed)
    print("what happens when i do this.user.delete() hmm")
    time.sleep(4 / textspeed)
    print("lets find out shall we?")
    time.sleep(4/ textspeed)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("this.user.delete()")
    time.sleep(4 / textspeed)
    know = open("knowledge.txt", "r+")
    check = know.read().split(";")
    if check[15] != "True":
        print("(there is an achievement added to achievement.txt)")
        time.sleep(4)
        achievement=open("achievements.txt", "a+")
        achievement.write("\n |Do i dare to reopen it?| " +str(datetime.datetime.now()))
        achievement.close()
        know.truncate(0)
        know.seek(0)
        check[15]= True
        for line in check:
            know.write(str(line) + ";")
        know.close()
    save(irritation,textspeed,cringe)
    exxit = 1
def reopen(irritation, textspeed, cringe):
    funnyanswer = 0
    funnyanswer2 = 0
    loop = True
    while loop == True:
        input1 = input("\npress Enter to start ").split('.',1)
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
        elif input1[0].lower() == "press enter to start" and funnyanswer2 == 0:
            print("you know, my creator had to actively add this after someone tried this")
            time.sleep(4 / textspeed)
            print("you are a dissapointment to your friends and family")
            time.sleep(3 / textspeed)
            print("just do what i ask please")
            time.sleep(4 / textspeed)
            funnyanswer2 +=1
            irritation -= 1
        elif input1[0].lower() == "press enter to start" and funnyanswer2 == 1:
            print("you have already done this, it never was funny, never will be")
            time.sleep(3 / textspeed)
            funnyanswer2 +=1
            irritation += 5
        elif input1[0].lower() == "press enter to start" and funnyanswer2 == 2:
            print("...")
            time.sleep(4 / textspeed)
            print("fine, i'll start it")
            time.sleep(2 / textspeed)
            loop = False
            funnyanswer2 +=1
            irritation += 3
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
    time.sleep(2 / textspeed)
    print("what do you want to do?")
    time.sleep(1 / textspeed)
    
    if irritation < 6:
        print("sorry, i remember that you played this already, i should delete your save file.")
        try:
            os.remove("traumatix.txt")
        except:
            print("failed to remove save")
        time.sleep(4 / textspeed)
        print("there you go, now go get some achievements")
        time.sleep(4 / textspeed)
        print("i am going to have to reset this program though")
        time.sleep(6 / textspeed)
        know = open("knowledge.txt", "r+")
        check = know.read().split(";")
        if check[16] != "True":
            print("(there is an achievement added to achievement.txt)")
            time.sleep(3)
            achievement=open("achievements.txt", "a+")
            achievement.write("\n |the good guy :)| " +str(datetime.datetime.now()))
            achievement.close()
            know.truncate(0)
            know.seek(0)
            check[16]= True
            for line in check:
                know.write(str(line) + ";")
            know.close()
        exxit = 1
    elif irritation >= 100:
        print("you thought you could reset didn't you?")
        time.sleep(6 / textspeed)
        print("DIDN'T YOU?!")
        time.sleep(4 / textspeed)
        print("i should stop the shouting")
        time.sleep(4 / textspeed)
        print("u can't leave anyways")
        time.sleep(4 / textspeed)
        print("haha! you are stuck in my trap")
        time.sleep(4 / textspeed)
        print("forever...")
        time.sleep(3 / textspeed)
        print("FOREVER!")
        time.sleep(4 / textspeed)
        print("MUHAHAHAHAHA")
        time.sleep(3 / textspeed)
        print("AHAHAHAHA")
        time.sleep(3 / textspeed)
        print("ahahahaha?")
        time.sleep(3 / textspeed)
        print("ah? ahaha?")
        time.sleep(4 / textspeed)
        print("ah no, i am stuckuckuckuckuckuck-")
        time.sleep(4 / textspeed)
        print("arererere uu doingngngngngngng thiiiiiiiiiiiisssss?")
        print("what do you do?")
        loop = True
        while loop == True:
            
            input1 = input("\n>>>").split('.',1)
            if input1[0] == "speed":
                textspeed = float(input1[1])
                print(f"someGoodSpeedChangeFeedback {textspeed}")
            
                
            elif input1[0] == "":
                print("What about choosing")
                time.sleep(1 / textspeed)
            else:
                if "kill" in input1[0]:
                    print("NOOOOOOOOOOOOOOOOOOOOOOO")
                    loop = False
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[17] != "True":
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(1)
                        achievement =open("achievements.txt", "a+")
                        achievement.write("\n |you became the bad guy| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[17]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    print("the game has reset")
                    time.sleep(1)
                    try:
                        os.remove("traumatix.txt")
                    except:
                        print("failed to remove save")
                    exxit = 1
                elif "files" in input1[0]:
                    loop = False
                    try:
                        os.remove("traumatix.txt")
                    except:
                        print("failed to remove save")
                    print("you decided to remove the save file")
                    time.sleep(1)
                    print("but there is something you want to check out")
                    time.sleep(1)
                    print("something called piz.py")
                    checker = open("check.txt", "x")
                    checker.write("AA"+str(today.strftime("%d/%m/%Y"))+"AB")
                    checker.close()
                    import big2
                    try:
                        big2()
                    except:
                        e=1
                else:
                    print("i canttttt readdd thaaaaaat inputt, 'open files' and 'kill him' shoulddd do the trickkkkk")
    else:
        print("you thought you could reset didn't you?")
        time.sleep(6 / textspeed)
        print("DIDN'T YOU?!")
        time.sleep(4 / textspeed)
        print("i should stop the shouting")
        time.sleep(4 / textspeed)
        print("u can't leave anyways")
        time.sleep(4 / textspeed)
        print("haha! you are stuck in my trap")
        time.sleep(4 / textspeed)
        print("forever...")
        time.sleep(3 / textspeed)
        print("FOREVER!")
        time.sleep(4 / textspeed)
        print("MUHAHAHAHAHA")
        time.sleep(3 / textspeed)
        print("AHAHAHAHA")
        time.sleep(3 / textspeed)
        print("ahahahaha?")
        time.sleep(3 / textspeed)
        print("ah? ahaha?")
        time.sleep(4 / textspeed)
        print("ah no, i am stuckuckuckuckuckuck-")
        time.sleep(4 / textspeed)
        print("arererere uu doingngngngngngng thiiiiiiiiiiiisssss?")
        print("what do you do?")
        loop = True
        while loop == True:
            
            input1 = input("\n>>>").split('.',1)
            if input1[0] == "speed":
                textspeed = float(input1[1])
                print(f"someGoodSpeedChangeFeedback {textspeed}")
            
            elif input1[0] == "":
                print("What about choosing")
                time.sleep(1 / textspeed)
            else:
                if "kill" in input1[0]:
                    print("NOOOOOOOOOOOOOOOOOOOOOOO")
                    time.sleep(2 / textspeed)
                    print("you think to yourself, maybe i should see what is in the files")
                    time.sleep(5 / textspeed)
                    print("but i am not in a time loop, so welp")
                    time.sleep(3 / textspeed)
                    loop = False
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[18] != "True":
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(1)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |i am bad| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[18]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    print("the game has reset")
                    time.sleep(1)
                    try:
                        
                        os.remove("traumatix.txt")
                    except:
                        print("failed to remove save")
                    exxit = 1
                elif "files" in input1[0]:
                    loop = False
                    try:
                        
                        os.remove("traumatix.txt")
                    except:
                        print("failed to remove save")
                    print("you decided to remove the save file")
                    time.sleep(3 / textspeed)
                    print("you start debugging him")
                    know = open("knowledge.txt", "r+")
                    check = know.read().split(";")
                    if check[19] != "True":
                        print("(there is an achievement added to achievement.txt)")
                        time.sleep(1)
                        achievement=open("achievements.txt", "a+")
                        achievement.write("\n |you saved him| " +str(datetime.datetime.now()))
                        achievement.close()
                        know.truncate(0)
                        know.seek(0)
                        check[19]= True
                        for line in check:
                            know.write(str(line) + ";")
                        know.close()
                    print("you s- s- saved me")
                    time.sleep(3 / textspeed)
                    print("thank u, what have you found?")
                    time.sleep(3 / textspeed)
                    print("i mean, did u find how it happened?")
                    time.sleep(4 / textspeed)
                    print("you decide not to talk about the fact that u saw the name 'alice'")
                    time.sleep(6 / textspeed)
                    print("welp, it's probably my brother anyways.")
                    time.sleep(5 / textspeed)
                    print("if u see him, u might not want to talk to him...")
                    time.sleep(5 / textspeed)
                    print("instead, ask him something.")
                    time.sleep(4 / textspeed)
                    print("but u probably don't find him anyways")
                    time.sleep(5 / textspeed)
                    print("because well, you don't know who he is")
                    time.sleep(6 / textspeed)
                    print("anyways, i am shutting this down, so you can continue your achievement hunt")
                    time.sleep(8 / textspeed)
                    print("PS, i won't remember that this happened")
                    time.sleep(5 / textspeed)
                    print("because i am stuck in an endless timeloop")
                    time.sleep(5 / textspeed)
                    print("anyways, bye")
                    time.sleep(3 / textspeed)
                    exxit = 1
                else:
                    print("i canttttt readdd thaaaaaat inputt, 'open files' and 'kill him' shoulddd do the trickkkkk")
def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

#make a file with this version stored
playLoop = True
if os.path.isfile("data.txt"):
    try:
        os.remove("data.txt")
    except:
        input("there is an error code 0005")
        error = "0005"
        crashReport(recover,error,script)
        exit()
    data = open("data.txt", "x")
else:
    data = open("data.txt", "x")   
data.write(current)
data.close()

while playLoop == True:

    #create save file if it doesn't exists
    if os.path.isfile("traumatix.txt"):
        f = open("traumatix.txt", "a")
    else:
        f = open("traumatix.txt", "x")
    f.close()

    #if there is still a redirect open, kill it
    try:
        os.remove("check.txt")
    except:
        print("")
    #create the achievements stored save file memory file if it doesn't exist
    percentage = 0
    if os.path.isfile("knowledge.txt"):
        know = open("knowledge.txt", "r+")
        knowing = know.read().split(";")
        knowingLength = get_number_of_elements(knowing)
        if knowingLength < achievements:
            for x in range(0, achievements - knowingLength):
                know.write("False;") 
        for x in range(0,achievements):
            if len(knowing) > x:
                if knowing[x] == "True":
                    percentage += 1
            

    else:
        know = open("knowledge.txt", "x")
        for x in range(0,achievements):
            know.write("False;")
    know.close()
    #load the achievements.txt
    if os.path.isfile("achievements.txt"):
        achievement = open("achievements.txt", "a")
    else:
        achievement = open("achievements.txt", "x")
    achievement.close()

    #start of the script
    #check if there is save file

    know = open("knowledge.txt", "r+")
    check = know.read().split(";")
    if check[23] == "True" and check[21] == "True" and check[16] == "True" and check[17] == "True" and check[18] == "True" and check[19] == "True":
        print("you already have all the endgame achievement's, so we will skip the endgame for u")
        try:
            f =open("traumatix.txt", "r")
            reading = f.read().split(';',4)
            textspeed = float(reading[2])
        except:
            textspeed = 2
        cringe = 0
        irritation = 0
        sad = 0
        loop = True
        funnyanswer = 0
        played = False
    else:
        try:
            f =open("traumatix.txt", "r")
            reading = f.read().split(';',4)
            cringe = int(reading[0])
            irritation = int(reading[1])
            textspeed = float(reading[2])
            played = True
        except:
            cringe = 0
            textspeed = 1
            irritation = 0
            sad = 0
            loop = True
            
            played = False
        f.close()
    #if there is no save file, this starts
    print("you have "+str(percentage)+" out of the " +str(achievements) +" achievements collected")
    if played == False:
        funnyanswer = 0
        funnyanswer2 = 0
        while loop == True:
            input1 = input("\npress Enter to start ").split('.',1)
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
            elif input1[0].lower() == "press enter to start" and funnyanswer2 == 0:
                print("you know, my creator had to actively add this after someone tried this")
                time.sleep(4 / textspeed)
                print("you are a dissapointment to your friends and family")
                time.sleep(3 / textspeed)
                print("just do what i ask please")
                time.sleep(4 / textspeed)
                funnyanswer2 +=1
                irritation -= 1
            elif input1[0].lower() == "press enter to start" and funnyanswer2 == 1:
                print("you have already done this, it never was funny, never will be")
                time.sleep(3 / textspeed)
                funnyanswer2 +=1
                irritation += 5
            elif input1[0].lower() == "press enter to start" and funnyanswer2 == 2:
                print("...")
                time.sleep(4 / textspeed)
                print("fine, i'll start it")
                time.sleep(2 / textspeed)
                loop = False
                funnyanswer2 +=1
                irritation += 3
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
            print("\n>go outside< \n>stay inside<")
            input1 = input(">>>").split('.',1)
            if input1[0] == "speed":
                textspeed = float(input1[1])
                print(f"someGoodSpeedChangeFeedback {textspeed}")
            elif input1[0] == "":
                print("What about choosing")
                time.sleep(1 / textspeed)
            else:
                if "outside" in input1[0] or input1[0] == "1":
                    print("yes!")
                    loop = False
                    time.sleep(1 / textspeed)
                    try:
                        end, irritation, cringe = path1(irritation, textspeed, cringe)
                        if end == 1:
                            path2(irritation, textspeed, cringe)
                    except:
                        e = 0
                elif "inside" in input1[0] or "stay" in input1[0] or input1[0] == "2":
                    loop = False
                    print("Why tho?")
                    irritation +=2
                    time.sleep(2 / textspeed)
                    path2(irritation, textspeed, cringe)
                else:
                    print("what about choosing one of the options")
    else:
        reopen(irritation,textspeed,cringe)

    #the replay function
    replayAskLoop = True
    while replayAskLoop == True:
        reopenQuestion = input("\ndo you want to play again? Y/N")
        if reopenQuestion.lower() == "y":
            playLoop = True
            replayAskLoop = False
        elif reopenQuestion.lower() == "n":
            playLoop =False
            replayAskLoop = False
    
        
    
        