antwoord1 = input("is de kaas geel? >>>")
if antwoord1 == "ja":
    antwoord2 = input("zitten er gaten in? >>>")
    if antwoord2 == "ja":
        antwoord3 = input("is de kaas belachelijk duur? >>>")
    else:
        antwoord4 = input("is de kaas hard als steen? >>>")
else:
    antwoord5 = input("heeft de kaas blauwe schimmels? >>>")
    antwoord6 = input("heeft de kaas een korst? >>>")
    
        
kaas = input("welke kaas is het? >>>")
if kaas == "emmenthaler":
    print(f"dus je had {kaas} in gedachten, antwoord 1 is "+str(antwoord1=="ja")+" geantwoord, antwoord 2 is "+str(antwoord2=="ja")+" geantwoord en antwoord 3 is "+str(antwoord3=="ja")+" geantwoord")
elif kaas == "leerdammer":
    print(f"dus je had {kaas} in gedachten, antwoord 1 is "+str(antwoord1=="ja")+" geantwoord, antwoord 2 is "+str(antwoord2=="ja")+" geantwoord en antwoord 3 is "+str(antwoord3=="nee")+" geantwoord")
elif kaas == "pemnigiano reggiano":
    print(f"dus je had {kaas} in gedachten, antwoord 1 is "+str(antwoord1=="ja")+" geantwoord, antwoord 2 is "+str(antwoord2=="nee")+" geantwoord en antwoord 3 is "+str(antwoord3=="ja")+" geantwoord")
elif kaas == "goudse kaas":
    print(f"dus je had {kaas} in gedachten, antwoord 1 is "+str(antwoord1=="ja")+" geantwoord, antwoord 2 is "+str(antwoord2=="nee")+" geantwoord en antwoord 3 is "+str(antwoord3=="nee")+" geantwoord")
elif kaas == "bleu de rochbaron":
    print(f"dus je had {kaas} in gedachten, antwoord 1 is "+str(antwoord1=="nee")+" geantwoord, antwoord 2 is "+str(antwoord2=="ja")+" geantwoord en antwoord 3 is "+str(antwoord3=="ja")+" geantwoord")
elif kaas == "foume d'ambert":
    print(f"dus je had {kaas} in gedachten, antwoord 1 is "+str(antwoord1=="nee")+" geantwoord, antwoord 2 is "+str(antwoord2=="ja")+" geantwoord en antwoord 3 is "+str(antwoord3=="nee")+" geantwoord")
elif kaas == "camembert":
    print(f"dus je had {kaas} in gedachten, antwoord 1 is "+str(antwoord1=="nee")+" geantwoord, antwoord 2 is "+str(antwoord2=="nee")+" geantwoord en antwoord 3 is "+str(antwoord3=="ja")+" geantwoord")
elif kaas == "mozzarella":
    print(f"dus je had {kaas} in gedachten, antwoord 1 is "+str(antwoord1=="nee")+" geantwoord, antwoord 2 is "+str(antwoord2=="nee")+" geantwoord en antwoord 3 is "+str(antwoord3=="nee")+" geantwoord")