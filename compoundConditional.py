#Andrew Parker
#9/14/17
#compoundConditionalDemo.py - and/or

num = float(input('Enter a number: '))

if num > 0 and num%7 == 0:
    print('number is positive and divisible by 7')
elif num > 0:
    print('Your number is positive and not divisible by 7  :( ')
elif num < 0 and num%7 == 0:
    print('Your number is negetive and divisible by 7  :( ')
elif num < 0:
    print('Your number is negetive and not divisible by 7  :( ')
else:
    print('your number is zero')
