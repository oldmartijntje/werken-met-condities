# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #uitrekenen of je meer hebt betaald dan wat je moest betalen

if change > 0: #kijken of je meer hebt betaald dan wat je moest betalen
  coinValue = 500 #het startgetal van hoeveel je terug kreeg
  
  while change > 0 and coinValue > 0: #zolang je nog niet je geld terug hebt en je nog niet door alle opties heen bent
    nrCoins = change // coinValue #kijken hoeveel je kan halen van de munt soort

    if nrCoins > 0: #kijken of het overige getal munten nog bestaat
      if coinValue >= 100:
        print('return maximal ', nrCoins, ' coins of ', coinValue/100, ' euros!' ) #zeggen hoeveel je kan ophalen van bepaalde munt
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue/100) +  ' euros did you return? ')) #hoeveel kreeg je terug van die munt
      else:
        print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #zeggen hoeveel je kan ophalen van bepaalde munt
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #hoeveel kreeg je terug van die munt
      
      change -= nrCoinsReturned * coinValue #

# comment on code below:
    if coinValue == 500:
          coinValue = 300
    elif coinValue == 300:
          coinValue = 200 
    elif coinValue == 200:
          coinValue = 100
    elif coinValue == 100:
          coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #kijk of er nog geld over is
  if change >= 100:
    fullchange = change % 100
    if change % 100 == 0:
          print('Change not returned: ', str(change/100) + ' euros')
    else:
          print('Change not returned: ', str((change - fullchange)/100) + ' euros and ', str(fullchange)+ ' cents')
  else:
        print('Change not returned: ', str(change) + ' cents')
else:
  print('done')