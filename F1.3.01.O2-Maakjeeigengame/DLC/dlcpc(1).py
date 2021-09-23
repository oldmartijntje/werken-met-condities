time = 0
weekNamen = ["ma","di","wo","do","vr","za","zo"]
while True:
    dag =input("zeg een dav van de week: ma = maandag, wo = woensdag")
    if dag in weekNamen:
        break
    else:
        print("das geen dag")   
while True:
    if dag != weekNamen[time]:
        print(weekNamen[time])
    else:
        print(weekNamen[time])
        break  
    time+=1