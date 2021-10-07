def table(number: int):
    for x in range(1,11):
        yeet = int(x)*int(number)
        print(f"{x} times {number} is " +str(yeet))
inputAnswer = input("from what number do you want to see the table?")
table(inputAnswer)