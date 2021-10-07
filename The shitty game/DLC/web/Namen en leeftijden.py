def identificatie(naam:str,leeftijd:int):
    print(f"\nthe name of this person is {naam} and their age is {leeftijd}\n")
print("say stop to stop")
while True:
    name = input("what is their name?")
    if name == "stop":
        break
    age = input(f"what is {name} their age?")
    if age == "stop":
        break
    intAge = int(age)
    identificatie(name,intAge)
