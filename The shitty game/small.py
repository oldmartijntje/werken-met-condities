import time
import datetime
import os.path
import os
from datetime import date
today = date.today()
script = "small.py"
current = "qwfj6qfnadlfa3242flakn62laga"
pissa = 0
recover = list()
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
        crash.write(f"no.sav//\n")
    else:
        if trauma !="":
            crash.write(f"{trauma}\n")
    crash.write(f"you know, it's really unfortunite, but by showing this to a DEV, it will probably get patched.\n")
    crash.write(f"ERROR CODE {error}/DATE:"+str(datetime.datetime.now())+f"/{script}/{current}\n")
    crash.write(f"{recover}\n\n\n\n\n")
    crash.close()
#check if version file sxists and if it is the same

if os.path.isfile("data.txt"):
    data = open("data.txt","r")
    dataa = data.read().split(";")
    data.close()
    if dataa[0] == current:
        e = 4
    else:
        input("there is an error code 0006")
        error = "0006"
        crashReport(recover,error,script)
        exit()
else:
    input("there is an error code 0007")
    error = "0007"
    crashReport(recover,error,script)
    exit()
#check if the main program sent you to this script, or if someone just opened this one

if os.path.isfile("check.txt"):
    checker = open("check.txt","r+")
    checkCheck = checker.read()
    if checkCheck == "AA"+str(today.strftime("%d/%m/%Y"))+"AC":
        checker.close()
    
        
    else:       
        error = "0004"
        crashReport(recover,error,script)
        input("there is an error code 0004")
        exit()
else:
    error = "0001"
    crashReport(recover,error,script)
    input("there is an error code 0001")
    exit()
#try to remove the redirect to this script, so no one can open it multiple times or change it
checker.close()
try:
    os.remove("check.txt")
except:
    error = "0002"
    crashReport(recover,error,script)
    input("there is an error code 0002\nTo protect against threats, the program has to be shutdown")
    exit()
#load achievements.txt
if os.path.isfile("achievements.txt"):
    achievement = open("achievements.txt", "a")
else:
    achievement = open("achievements.txt", "x")
achievement.close

#just the script for the other exersice
vraag9 = 0
vraag8 = 0
vraag10 = 0
vraag11= 0
vraag12= 0
print("+++++++++++++++++++++++++++++++")
print("good that you are here")
print("we have a few questions for you")
print("+++++++++++++++++++++++++++++++")
pizza = input("do you want to order pizza? Y/N")
if pizza == "Y" or pizza == "y":
    pissa = 1
    #redirect to the next script
    checker = open("knowledge.txt", "x")
    checker.write("AA"+str(datetime.datetime.now())+"AD")
    checker.close()
    try:
        import big1
    
        big1()
    except:
        e = 3
if pissa == 0:    
    input("have you beaten the enderdragon?Y/N")
    vraag1 = int(input("how many years do you have practical experience with dressage?"))
    vraag2 = int(input("how many years do you have practical experience with juggling?"))
    input("do you want the job?Y/N")
    vraag3 = int(input("how many years do you have practical experience with acrobatics?"))
    vraag4 = input("do you have a MBO-4 Diploma? Y/N")
    vraag5 = input("do you own a truck driver's license? Y/N")
    input("does santaclaus exist?Y/N")
    vraag6 = input("do you own a tall hat? Y/N")
    input("how many people have you killed?")
    vraag7 = input("have you been born as a Male or as a Female? M/F")
    if vraag7 == "m" or vraag7 == "M":
        vraag8 = input("do you have a mustache? Y/N")
        if vraag8 == "y" or vraag8 =="Y":
            vraag9 = int(input("how tall is your mustache in CM?"))
        input("do you have a Hernia?Y/N")
    elif vraag7 == "f" or vraag7 == "F":
        vraag10 = input("what is your hair color? (r=red,b=blonde,ew = anything else)")
        vraag11 = input("what is your hairstyle? curled = C, braids = B,Bald = E")
        vraag12 = int(input("how tall is your hair in CM?"))
    input("how many kids do you have in your basement?")
    vraag13=int(input("how fat are you in KG?"))
    vraag14=int(input("how tall are you in CM?"))

    if vraag7 == "m" or vraag7 == "M":
        if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "Y" or vraag4 == "y") and (vraag5 == "Y" or vraag5 == "y") and (vraag6 == "Y" or vraag6 == "y") and (vraag8 == "Y" or vraag8 == "y") and vraag9 > 10 and vraag13 > 90 and vraag14 > 150:
            print("Congrats, you are a good canidate, we will call you.")
        else:
            print("Sorry, but ur not the man we are looking for, you better go empty my trash")
    elif vraag7 == "f" or vraag7 == "F":
        if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "y" or vraag4 == "Y") and (vraag5 == "y" or vraag5 == "Y") and (vraag6 == "y" or vraag6 == "Y") and vraag13 > 90 and vraag14 > 150 and (vraag10 == "r" or vraag10=="R") and (vraag11 == "C" or vraag11=="c") and vraag12 >20:
            print("Congrats, you are a good canidate, we will call you.")
        else:
            print("Nope, i think being stripper would fit a women like u more")
    #this is used for the achievement system
    know = open("knowledge.txt", "r+")
    check = know.read().split(";")
    if check[22] != "True":
        print("(there is an achievement added to achievement.txt)")
        time.sleep(4)
        achievement=open("achievements.txt", "a+")
        achievement.write("\n |Hmm i am hungry| " +str(datetime.datetime.now()))
        achievement.close
        know.truncate(0)
        know.seek(0)
        check[22]= True
        for line in check:
            know.write(str(line) + ";")
        know.close()
    print("you die from a heart attack")
    time.sleep(2)
    



