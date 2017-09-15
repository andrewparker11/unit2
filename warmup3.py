#Andrew Parker
#9/15/17
#warmup3

num = float(input('Please input a number'))

if num%3 and num%2:
    print('Your number is both divisible by 2 and 3' )
elif num%3:
     print('Your number is both divisible by 3' )
elif num%2:
     print('Your number is both divisible by 2' )
else:
    print('neither' )
    