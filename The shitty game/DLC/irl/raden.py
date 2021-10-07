import random
loop = True
tries = 0
timesPlayed = 0
def randomInt():
    rando = random.randint(0, 1000)
    return rando
score = 0
print("\nwelcome my friends\n")
guessed = 0
while  True:
    guessed += 1
    rando = randomInt()
    print("random int chosen between 0 and 1000")
    tries = 0
    while tries < 10:
        while True:
            try:
                guess = int(input("well, why are u waiting, guess..."))
                break
            except:
                print("what about choosing a int (number)")
        difference = rando - guess
        if difference == 0:
            print("you got it!")
            score += 1
            break
        if difference >= -20 and difference <= 20:
            print("oh you are hot Af babe")
        elif difference >= -50 and difference <= 50:
            print("oh you are warm")
        else:
            print("not even close baby, Technoblade never dies!")
        if guess > rando:
            print("u might want to go lower")
        elif guess < rando:
            print("you might want to guess higher")
        tries += 1
        print("\n")
        if tries == 10:
            print("welp, u tried, it was:",rando)
    print("your score: "+str(score))
    timesPlayed+=1
    if timesPlayed == 20:
        break
    
    while True:
        nogEenKeertje = input("\ndo you wan't to try another one? Y/N").lower()
        if nogEenKeertje == "y":
            loop = True
            break
        elif nogEenKeertje == "n":
            loop = False
            break
        else:
            print("what about answering Y or N?")
    if loop == False:
        break
print("endscore: "+str(score))