import time
import datetime
import os.path
import os
if os.path.isfile("achievements.txt"):
    achievement = open("achievements.txt", "a")
else:
    achievement = open("achievements.txt", "x")
achievement.close
vraag9 = 0
vraag8 = 0
vraag10 = 0
vraag11= 0
vraag12= 0
print("+++++++++++++++++++++++++++++++")
print("leuk dat u solliciteerd voor de")
print("baan van Circusdirecteur voor")
print("Circus HotelDeBotel. we hebben")
print("een paar vraagjes voor u.")
print("+++++++++++++++++++++++++++++++")
pizza = input("wilt u een pizza bestellen? J/N")
if pizza == "J" or pizza == "j":
    import doNotRun
    
    doNotRun()
    
input("heeft u wel eens de enderdraak verslagen?J/N")
vraag1 = int(input("hoeveel jaar heeft u praktijkervaring met dieren-dressuur?"))
vraag2 = int(input("hoeveel jaar heeft u praktijkervaring met jongleren?"))
input("wilt u deze baan?J/N")
vraag3 = int(input("hoeveel jaar heeft u praktijkervaring met acrobatiek?"))
input("simp je voor loki?J/N")
vraag4 = input("bezit u een Diploma MBO-4? J/N")
vraag5 = input("bezit u een vrachtwagen rijbewijs? J/N")
input("bestaat sinterklaas?J/N")
vraag6 = input("bezit u een hoge hoed? J/N")
input("hoeveel mensen heeft u vermoord?")
vraag7 = input("wat bent u als geboren? man of vrouw? M/V")
if vraag7 == "m" or vraag7 == "M":
    vraag8 = input("heeft u een snor? J/N")
    if vraag8 == "j" or vraag8 =="J":
        vraag9 = int(input("hoelang is uw snor in cm?"))
    input("heeft u een hernia?J/N")
elif vraag7 == "v" or vraag7 == "V":
    vraag10 = input("wat is uw haarkleur? (r=rood,b=blond,z=zwart)")
    vraag11 = input("wat voor haarstijl heeft u? krul=k,staartjes=s,kaal=a")
    vraag12 = int(input("hoe lang is uw haar in cm?"))
input("hoeveel kinderen heeft u in uw kelder?")
vraag13=int(input("wat is uw lichaamsgewicht in kg?"))
vraag14=int(input("hoe lang bent u in cm?"))

if vraag7 == "m" or vraag7 == "M":
    if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "J" or vraag4 == "j") and (vraag5 == "J" or vraag5 == "j") and (vraag6 == "J" or vraag6 == "j") and (vraag8 == "J" or vraag8 == "j") and vraag9 > 10 and vraag13 > 90 and vraag14 > 150:
        print("Gefeliciteerd, u bent een goede kanidaat. stuur nu uw cv maar door")
    else:
        print("Nope, u bent niet in aanmerking gekomen voor deze beropespositie.")
elif vraag7 == "v" or vraag7 == "V":
    if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "J" or vraag4 == "j") and (vraag5 == "J" or vraag5 == "j") and (vraag6 == "J" or vraag6 == "j") and vraag13 > 90 and vraag14 > 150 and (vraag10 == "r" or vraag10=="R") and (vraag11 == "k" or vraag11=="K") and vraag12 >20:
        print("Gefeliciteerd, u bent een goede kanidaat. stuur nu uw cv maar door")
    else:
        print("Nope, u bent niet in aanmerking gekomen voor deze beroepspositie.")
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
exit()



