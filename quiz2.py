#Andrew Parker
#9/25/17
#quiz2.py - Analyzes two numbers and quizes you on them

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a second number: '))
if num1>num2:
    print('The first number is bigger' )
elif num2>num1:
    print('The second number is bigger' )
elif num1==num2:
    print('The numbers are the same' )
elif num1%3 or num2%3 == 0:
    print('Both numbers are divisible by 3')
elif num1%3 == 0:
    print('Only the first number is divisible by 3')
elif num2%3 == 0:
    print('Only the second number is divisible by 3')
else:
    print('Neither number is divisible by 3')
    
product = int(input('What is the product of your two numbers?' ))
if product == num1*num2:
    print('Correct' )
else:
    print('Incorrect' )
