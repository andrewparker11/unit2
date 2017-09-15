#Andrew Parker
#9/15/17
#warmup3

num = float(input('Please input a number '))


if num%3 == 0:
     print('Your number is divisible by 3' )
elif num%2 == 0:
     print('Your number is divisible by 2' )
elif num%3 == 0 and num%2 == 0:
    print('Your number is both divisible by 2 and 3' )
else:
    print('neither' )
    