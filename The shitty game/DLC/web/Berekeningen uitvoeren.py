import random

#print(random.randint(3, 9))
def addition(number1:int=10, number2:int=12):
    print(f"{number1} + {number2} = "+str(number1+number2))
def subtraction(number1:int=58, number2:int=34):
    print(f"{number1} - {number2} = "+str(number1-number2))
def multiplication(number1:int=6, number2:int=7):
    print(f"{number1} x {number2} = "+str(number1*number2))
def division(number1:int=144, number2:int=12):
    print(f"{number1} : {number2} = "+str(number1/number2))
def increment(number:int=12):
    print(f"{number} + 1 = "+str(number+1))
def decrement(number:int=34):
    print(f"{number} - 1 = "+str(number-1))
for x in range (1,4):
    addition(random.randint(0, 69),random.randint(0, 69))
    subtraction(random.randint(0, 69),random.randint(0, 69))
    multiplication(random.randint(0, 69),random.randint(0, 69))
    division(random.randint(0, 69),random.randint(1, 69))
    increment(random.randint(0, 69))
    decrement(random.randint(0, 69))