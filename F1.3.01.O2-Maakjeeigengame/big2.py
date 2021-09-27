import time
import datetime
import os.path
import os
from datetime import date
today = date.today()
current = "qwfj6qfnadlfa3242flakn62laga"
script = "big2.py"
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
#see if there is a save file
#do remove if not in part 2


#check if version file sxists and if it is the same
if os.path.isfile("data.txt"):
    data = open("data.txt","r")
    dataa = data.read().split(";")
    data.close()
    if dataa[0] == current:
        e = 4
    else:
        error = "0006"
        crashReport(recover,error,script)
        input("there is an error code 0006")
        exit()
else:
    error = "0007"
    crashReport(recover,error,script)
    input("there is an error code 0007")
    exit()       

#check if the main program sent you to this script, or if someone just opened this one
if os.path.isfile("check.txt"):
    checker = open("check.txt","r+")
    checkCheck = checker.read()
    if checkCheck == "AA"+str(today.strftime("%d/%m/%Y"))+"AB":
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

if os.path.isfile("achievements.txt"):
    achievement = open("achievements.txt", "a")
else:
    achievement = open("achievements.txt", "x")
achievement.close

#dit berekent de prijs per pizza
def calculateCosts(dough, pepperoni, cheese, pineapple, ham, tomatosauce, tuna):
    price = 0
    #grootte van pizza
    if dough == "small":
        price += 1
    if dough == "medium":
        price += 1.5
    if dough == "large":
        price += 2
    #als humongous gekozen is, kies large
    if dough == "humongous":
        price += 2
    #aantal pepperoni
    if pepperoni == "small":
        price += 0.4
    if pepperoni == "medium":
        price += 0.6
    if pepperoni == "large":
        price += 0.9
    if pepperoni == "humongous":
        price += 9
    #aantal kaas
    if cheese == "small":
        price += 0.2
    if cheese == "medium":
        price += 0.3
    if cheese == "large":
        price += 0.45
    if cheese == "humongous":
        price += 4.5
        #aantal pineapple
    if pineapple == "small":
        price += 0.2
    if pineapple == "medium":
        price += 4
    if pineapple == "large":
        price += 16
    if pineapple == "humongous":
        price += 256
        #aantal ham
    if ham == "small":
        price += 0.2
    if ham == "medium":
        price += 4
    if ham == "large":
        price += 16
    if ham == "humongous":
        price += 256
        #aantal tomaten saus
    if tomatosauce == "small":
        price += 0.1
    if tomatosauce == "medium":
        price += 0.2
    if tomatosauce == "large":
        price += 0.3
    if tomatosauce == "humongous":
        price += 0.5
        #aantal tonijn
    if tuna == "small":
        price += 1.2
    if tuna == "medium":
        price += 1.5
    if tuna == "large":
        price += 1.9
    if tuna == "humongous":
        price += 19
    return price
#maakt random pizzas
def randomTopping():
    from random import randrange
    number = (randrange(9))
    if number == 0 or number == 7:
        returnValue = "small"
    if number == 1 or number == 6:
        returnValue = "medium"
    if number == 2 or number == 5:
        returnValue = "large"
    if number == 3 or number == 4:
        returnValue = "humongous"
    if number == 8:
        returnValue = "NONE"
    return returnValue

#dit is de setup zodat de rest werkt
import os.path
try:
    os.remove("pizCalc3.txt")
except:
    fd=2
try:
    os.remove("pizCalc2.txt")
except:
    fd=1
try:
    os.remove("pizCalc1.txt")
except:
    fd=4
loop = True
round = 1
round2 = 1
totalcosts = 0
pizzaAmount = "startup"
randomized = "no"
keepRandomized = "no"
import os
know = open("knowledge.txt", "r+")
check = know.read().split(";")
if check[23] != "True":
    print("(there is an achievement added to achievement.txt)")
    time.sleep(3)
    print("(there is an achievement added to achievement.txt)")
    time.sleep(3)
    achievement=open("achievements.txt", "a+")
    achievement.write("\n |PIZZAAA| " +str(datetime.datetime.now()))
    achievement.close
    know.truncate(0)
    know.seek(0)
    check[21]= True
    for line in check:
        know.write(str(line) + ";")
    know.close()
#dit is een loop die je blijft vragen of je meer wilt bestellen en of je de menu kaart wilt zien
while loop == True:
    menukaart = input("do you want to look at the menu? >>>")
    if menukaart == "yes" or menukaart == "Yes":
        print("----------------------------------------------------------")   
        print("|             |  small  |  medium  |  large  | humongous | humangous==10*large") 
        print("|    Dough    |   €1    |   €1.5   |    €2   |           |") 
        print("|  Pepperoni  |  €0.4   |   €0.6   |   €0.9  |     €9    |")
        print("|   Cheese    |  €0.2   |   €0.3   |  €0.45  |    €4.5   |")
        print("|  pinapple   |  €0.2   |    €4    |   €16   |    €256   |")
        print("|    ham      |  €0.2   |    €4    |   €16   |    €256   |")
        print("| tomatosauce |  €0.1   |   €0.2   |  €0.3   |    €0.5   |")
        print("|    tuna     |  €1.2   |   €1.5   |  €1.9   |    €19    |")
        print("----------------------------------------------------------")   
    try:
        pizzaAmount = int(input("how many pizzas? >>>"))
    except:
        print("maybe try putting in a number next time")
    if pizzaAmount != "startup":
        if pizzaAmount > 0:

            #dit blijft herhalen tot het zoveel keer heeft herhaald als het aantal pizza's
            while round <= pizzaAmount:
                round += 1

                #check if file4 exists
                if os.path.isfile("pizCalc4.txt"):
                    file4 = open("pizCalc4.txt", "a")
                else:
                    file4 = open("pizCalc4.txt", "x")
                file4.close()
                file4 = open("pizCalc4.txt", "r")
                allowRandom = file4.read()

                #dit bekijkt of het al de 2e ronde is, want als je al een ronde bent geweest kan je de input skippen om de zelfde configuratie als de vorige pizza te nemen
                if round > 2:
                    if keepRandomized == "yes" or keepRandomized == "Yes":
                        dough = randomTopping()
                        pepperoni = randomTopping()
                        cheese = randomTopping()
                        pineapple = randomTopping()
                        ham = randomTopping()
                        tomatosauce= randomTopping()
                        tuna = randomTopping()
                        print(round)
                    else:     
                        again = input("do you want to repeat the last order? >>>")
                        if again == "yes" or again == "Yes":
                            if randomized == "yes" or randomized == "Yes":
                                keepRandomized = input("do you want to randomize all? >>>")
                                if keepRandomized == "yes" or keepRandomized == "Yes":
                                    dough = randomTopping()
                                    pepperoni = randomTopping()
                                    cheese = randomTopping()
                                    pineapple = randomTopping()
                                    ham = randomTopping()
                                    tomatosauce= randomTopping()
                                    tuna = randomTopping()
                                else:
                                    dough = randomTopping()
                                    pepperoni = randomTopping()
                                    cheese = randomTopping()
                                    pineapple = randomTopping()
                                    ham = randomTopping()
                                    tomatosauce= randomTopping()
                                    tuna = randomTopping()
                            else:
                                print("Okay")

                        #hier vul je in welke topping je wilt als je een andere pizza wilt
                        else:
                            if allowRandom == "yes":
                                randomized = input("do you want to randomize the order? >>>")
                            if randomized == "yes" or randomized == "Yes":
                                dough = randomTopping()
                                pepperoni = randomTopping()
                                cheese = randomTopping()
                                pineapple = randomTopping()
                                ham = randomTopping()
                                tomatosauce= randomTopping()
                                tuna = randomTopping()

                            else:
                                print("for pizza number " + str(round -1) + ", which specifications do you want? U don't have to choose all things")
                                dough = input("Dough >>>")
                                pepperoni = input("Pepperoni >>>")
                                cheese = input("Cheese >>>")
                                pineapple = input("Pineapple >>>")
                                ham = input("Ham >>>")
                                tomatosauce = input("tomatosauce >>>")
                                tuna = input("Tuna >>>")

                #dit is voor de 1e pizza, waarbij je invult wat je wilt
                else:
                    if allowRandom == "yes":
                        randomized = input("do you want to randomize the order? >>>")
                    if randomized == "yes" or randomized == "Yes":
                        dough = randomTopping()
                        pepperoni = randomTopping()
                        cheese = randomTopping()
                        pineapple = randomTopping()
                        ham = randomTopping()
                        tomatosauce= randomTopping()
                        tuna = randomTopping()

                    else:
                        print("for pizza number " + str(round -1) + ", which specifications do you want? U don't have to choose all things")
                        dough = input("Dough >>>")
                        pepperoni = input("Pepperoni >>>")
                        cheese = input("Cheese >>>")
                        pineapple = input("Pineapple >>>")
                        ham = input("Ham >>>")
                        tomatosauce = input("tomatosauce >>>")
                        tuna = input("Tuna >>>")
                file4.close()

                #hier kijk je of de pizCalc2.txt bestaat, en zo niet, dan maakt het een nieuwe pizCalc2.txt
                if os.path.isfile("pizCalc2.txt"):
                    f = open("pizCalc2.txt", "a")
                else:
                    f = open("pizCalc2.txt", "x")

                #hier kijk je of de pizCalc1.txt bestaat, en zo niet, dan maakt het een nieuwe pizCalc1.txt
                if os.path.isfile("pizCalc1.txt"):
                    file2 = open("pizCalc1.txt", "a")
                else:
                    file2 = open("pizCalc1.txt", "x")

                #het aanroepen van de functie om de prijs van de pizza te berekenen
                costPerPizza = calculateCosts(dough, pepperoni, cheese, pineapple, ham, tomatosauce, tuna)
                #het uploaden naar een file
                file2.write(str(costPerPizza) + ",")

                #kijken of er dingen niet zijn gekozen
                if dough != "small" and dough != "medium" and dough != "large" and dough != "humongous":
                    dough = "NONE"
                if dough == "humongous":
                    dough = "large"
                if pepperoni != "small" and pepperoni != "medium" and pepperoni != "large" and pepperoni != "humongous":
                    pepperoni = "NONE"
                if cheese != "small" and cheese != "medium" and cheese != "large" and cheese != "humongous":
                    cheese  = "NONE"
                if pineapple != "small" and pineapple != "medium" and pineapple != "large" and pineapple != "humongous":
                    pineapple = "NONE"
                if ham != "small" and ham != "medium" and ham != "large" and ham != "humongous":
                    ham = "NONE"
                if tomatosauce != "small" and tomatosauce != "medium" and tomatosauce != "large" and tomatosauce != "humongous":
                        tomatosauce = "NONE"
                if tuna != "small" and tuna != "medium" and tuna != "large" and tuna != "humongous":
                    tuna = "NONE"
                f.write(dough + "," + pepperoni + "," + cheese + "," + pineapple + "," + ham + "," + tomatosauce + "," + tuna + ",")
                totalcosts += costPerPizza
                
                #sluiten van de files
                f.close()
                file2.close()

            #het afrekenen
            print("that will be an amount of €" + str(totalcosts))
            receipt = input("do you want the receipt? >>>")
            if receipt == "yes" or receipt == "Yes":
                while round2 <= pizzaAmount:
                    round2 += 1

                    #hier kijk je of de pizCalc3.txt bestaat, en zo niet, dan maakt het een nieuwe pizCalc3.txt
                    if os.path.isfile("pizCalc3.txt"):
                        receipt = open("pizCalc3.txt", "a")
                    else:
                        receipt = open("pizCalc3.txt", "x")
                    #openen van andere files

                    file1 = open("pizCalc2.txt", "r")
                    file2 = open("pizCalc1.txt", "r")
                    #data opslaan

                    lines1 = file1.read().split(',', 7)
                    lines2 = file2.read().split(',', 1)
                    file1.close()
                    file2.close()

                    #bonnetje schrijven naar file
                    receipt.write("-------------------------------------\n")
                    receipt.write("|Pizza  size|"+lines1[0]+ "|\n")
                    receipt.write("| Pepperoni |"+lines1[1]+ "|\n")
                    receipt.write("|  Cheese   |"+lines1[2]+ "|\n")
                    receipt.write("| Pineapple |"+lines1[3]+ "|\n")
                    receipt.write("|    Ham    |"+lines1[4]+ "|\n")
                    receipt.write("|Tomatosauce|"+lines1[5]+ "|\n")
                    receipt.write("|   Tuna    |"+lines1[6]+ "|\n")
                    receipt.write("-------------------------------------\n")
                    receipt.write("|   Price   | €"+str(lines2[0])+ "|\n")
                    if allowRandom == "yes":
                        print(round2)
                    #files verwijderen
                    del lines1[0]
                    del lines1[0]
                    del lines1[0]
                    del lines1[0]
                    del lines1[0]
                    del lines1[0]
                    del lines1[0]
                    del lines2[0]
                    #heropenen en herschrijven van files
                    file1 = open("pizCalc2.txt", "w+")
                    file2 = open("pizCalc1.txt", "w+")
                    for line in lines1:
                        file1.write(line + ",")
                    for line in lines2:
                        file2.write(line + ",")
                    
                    file1.close()
                    file2.close()
            
                receipt.write("-------------------------------------\n")
                receipt.write("|   Total   |€"+str(totalcosts)+ "|\n")
                receipt.close()
                receipt = open("pizCalc3.txt", "r")
                for x in receipt:
                    print(x.strip())
                receipt.close()
            else:
                print("okay")
            #zet de loop uit
            loop = False
            know = open("knowledge.txt", "r+")
            check = know.read().split(";")
            if check[21] != "True":
                print("(there is an achievement added to achievement.txt)")
                time.sleep(3)
                achievement=open("achievements.txt", "a+")
                achievement.write("\n |True Ending !2!| " +str(datetime.datetime.now()))
                achievement.close
                know.truncate(0)
                know.seek(0)
                check[21]= True
                for line in check:
                    know.write(str(line) + ";")
                know.close()
            print("congrats, this was the true ending!")
            input("input to close >>>")
            
            
        else:
            print("you need to atleast buy 1")

