import time
textspeed = 2
irritation = 0
sad = 0
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
        irritation += 1
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