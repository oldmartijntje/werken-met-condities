def game(rollen):
    rolle={0,1,1,0,0,1,0,0,0,1,0,2,0,0,1,0}
    from random import randrange
    shuffle = (randrange(16))
    playerrol = rolle[shuffle]



startmenu = True
game = True
while game == True:
    while startmenu == True:
        print("welkom bij weerwolven startmenu")
        print("start, help of stop")
        menu1 = input("")
        if menu1 != "stop" and menu1 != "start" and menu1 != "help":
            print("u moet een optie kiezen")
        else:
            startmenu = False
