import time
amount = 0
round = 50
while True:
    print(str(amount) +" + "+str(round)+" = "+str(amount+round))
    amount +=round
    round+=1
    time.sleep(0.5)
    if amount >= 1000:
        break